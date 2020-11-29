#include <stdio.h>
#include <stdlib.h>

typedef enum {CPY, INC, DEC, JNZ} Instructionset;

typedef struct Instruction_ {
	struct Instruction_ *next;
	struct Instruction_ *prev;
	Instructionset instruction;
	struct Instruction_ * (*do_instruction)(struct Instruction_ *pc, int registers[4]);
	char c1[5];
	char c2[5];
}Instruction;

typedef struct Instruction_ * (*ExecPtr)(struct Instruction_ *pc, int registers[4]);

Instruction *do_inc(Instruction *pc, int registers[4]);
Instruction *do_dec(Instruction *pc, int registers[4]);
Instruction *do_cpy(Instruction *pc, int registers[4]);
Instruction *do_jnz(Instruction *pc, int registers[4]);

ExecPtr exec_ptrs[5] = {
	&do_cpy,
	&do_inc,
	&do_dec,
	&do_jnz
};

int get_value(const char *in, int registers[4]) {
	int val = 0;
	if(*in < 'a')
		sscanf(in, "%d", &val);
	else
		val = registers[*in - 'a'];
	return val;
}

void add(int registers[4], int reg, int num) {
	if(reg >= 0)
		registers[reg] = registers[reg] + num;
}

Instruction *do_inc(Instruction *pc, int registers[4]) {
	add(registers, pc->c1[0] - 'a', 1);
	return pc->next;
}

Instruction *do_dec(Instruction *pc, int registers[4]) {
	add(registers, pc->c1[0] - 'a', -1);
	return pc->next;
}

Instruction *do_cpy(Instruction *pc, int registers[4]) {
	int value_from = get_value(pc->c1, registers);

	int register_to = pc->c2[0] - 'a';
	if(register_to >= 0)
		registers[register_to] = value_from;
	return pc->next;
}

Instruction *do_jnz(Instruction *pc, int registers[4]) {
	int cmp = get_value(pc->c1, registers);
	if(cmp == 0)
		return pc->next;

	int steps = get_value(pc->c2, registers);
	int inc = steps < 0 ? 1 : -1;
	for(int i = steps; i != 0 && pc != NULL; i += inc) {
		pc = steps < 0 ? pc->prev : pc->next;
	}
	return pc;
}

Instruction *add_command(Instruction *program, Instruction *instr) {
	if(program == NULL) {
		program = instr;
		return program;
	}
	Instruction *list = program;
	while(list->next != NULL) {
		list = list->next;
	}
	instr->prev = list;
	list->next = instr;
	return program;
}

void dump_registers(int registers[4]) {
	for(int i = 0; i < 4; i++) {
		printf("Register %c = %d\n", 'A' + i, registers[i]);
	}
}

Instruction *instruction_factory_create(int type, const char *buf) {
	Instruction *i = (Instruction *)malloc(sizeof(Instruction));
	i->next = NULL;
	i->prev = NULL;
	i->instruction = type;
	i->do_instruction = exec_ptrs[type];
	sscanf(buf, "%s %s", i->c1, i->c2);
	return i;
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(*(argv + 1), "r");
	int registers[4] = {0,0,0,0};
	Instruction *program = NULL;

	if(!fp) {
		fprintf(stderr, "FAIL!\n");
		exit(-1);
	}

	char *buf = (char *)calloc(255, 1);
	while( (buf = fgets(buf, 255, fp))) {
		if(*buf == 'c') {
			program = add_command(program, instruction_factory_create(CPY, buf + 4));
		}
		if(*buf == 'i') {
			program = add_command(program, instruction_factory_create(INC, buf + 4));
		}
		if(*buf == 'd') {
			program = add_command(program, instruction_factory_create(DEC, buf + 4));
		}
		if(*buf == 'j') {
			program = add_command(program, instruction_factory_create(JNZ, buf + 4));
		}
	}
	fclose(fp);

	Instruction *pc = program;
	while(pc != NULL) {
		pc = pc->do_instruction(pc, registers);
	}
	dump_registers(registers);

	Instruction *t = program;
	while(t != NULL) {
		Instruction *tmp = t->next;
		free(t);
		t = tmp;
	}
	free(buf);
	return 0;
}
