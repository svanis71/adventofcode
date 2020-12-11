#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include "mystring.h"

typedef enum {eBot,Output} Target;

typedef struct command {
	Target targetTypeLow;
	Target targetTypeHigh;
	int lowToNr;
	int highToNr;
} Command;

typedef struct _bot_ {
	struct _bot_ *next;
	Target type;
	int nr;
	int low;
	int high;
	Command *command;
} Bot;

Bot *create_new_bot(int bot_nr, int value);
Bot *find_bot(Bot *root, int bot_nr);
void give_to_bot(Bot *root, int bot_nr, int value);
void run_command(Bot *root, Bot *a_bot);
Bot *add_bot(Bot *root, Bot *new_item);
void dump_bot(Bot *root);
void add_command(Bot *root, int from_bot_nr, Target lowTarget, int low_nr, Target highTarget, int high_nr);
Bot *add_value_to_bot(Bot *root, int bot_nr, int value);
Bot *handle_input(Bot *root, const char *line);
Bot *handle_command(Bot *root, const char *line);

Bot *create_new_bot(int bot_nr, int value) {
	Bot *new_item = (Bot *)malloc(sizeof(Bot));
	new_item->nr = bot_nr;
	new_item->type = eBot;
	new_item->low = -1;
	new_item->command = NULL;
	new_item->high = value;
	new_item->next = NULL;
	return new_item;
}

Bot *find_bot(Bot *root, int bot_nr) {
	for(Bot *list = root; list != NULL; list = list->next) {
		if(list->type == eBot && bot_nr == list->nr) {
			return list;
		}
	}
	return NULL;
}

Bot *create_new_output(int nr, int value) {
	Bot *out = (Bot *)malloc(sizeof(Bot));
	out->type = Output;
	out->nr = nr;
	out->high = value;
}

Bot *find_output(Bot *root, int bot_nr) {
	for(Bot *list = root; list != NULL; list = list->next) {
		if(list->type == Output && bot_nr == list->nr) {
			return list;
		}
	}
	return NULL;
}

Bot *add_bot(Bot *root, Bot *new_item) {
	if(root == NULL) {
		return new_item;
	}
	Bot *list = root;
	Bot *tail = NULL;
	while(list != NULL) {
		tail = list;
		list = list->next;
	}
	tail->next = new_item;
	return root;
}

void dump_bot(Bot *root) {
	for(Bot *itm = root; itm != NULL; itm = itm->next) {
		if(itm->type == eBot)
			printf("Bot #%d\tHigh: %d\tLow: %d\n", itm->nr, itm->high, itm->low);
		else
			printf("Output #%d\tValue: %d\n", itm->nr, itm->high);
	}
}

void give_value_to_output(Bot *root, int nr, int value) {
	Bot *targetBot = find_output(root, nr);
	if(targetBot == NULL) {
		targetBot = add_bot(root, create_new_output(nr, value));
	}
	else {
		targetBot->high = value;
	}
}

void give_to_bot(Bot *root, int bot_nr, int value) {
	Bot *targetBot = find_bot(root, bot_nr);
	if(targetBot == NULL) {
		targetBot = add_bot(root, create_new_bot(bot_nr, value));
	}
	else {
		if(targetBot->low < 0 && targetBot->high < 0)
			targetBot->high = value;
		else if(targetBot->low < 0 && targetBot->high >= 0 && value > targetBot->high) {
			targetBot->low = targetBot->high;
			targetBot->high = value;
		}
		else {
			targetBot->low = value;			
		}
		if(targetBot->low == 17 && targetBot->high == 61)	
			printf("YES!!! Bot %d now has values %d and %d\n", targetBot->nr, targetBot->low, targetBot->high);
		run_command(root, targetBot);
	}
}

void run_command(Bot *root, Bot *a_bot) {
	if(a_bot->command != NULL && a_bot->low != -1 && a_bot->high != -1) {
		if(a_bot->command->targetTypeLow == eBot) {
			/*printf("Bot %d give bot %d value %d\n", a_bot->nr, a_bot->command->lowToNr, a_bot->low);*/
			give_to_bot(root, a_bot->command->lowToNr, a_bot->low);
			a_bot->low = -1;
		}
		if(a_bot->command->targetTypeHigh == eBot) {
			/*printf("Bot %d give bot %d value %d\n", a_bot->nr, a_bot->command->highToNr, a_bot->high);*/
			give_to_bot(root, a_bot->command->highToNr, a_bot->high);
			a_bot->high = -1;
		}
		if(a_bot->command->targetTypeLow == Output) {
			printf("LOW to %d output %d\n", a_bot->low, a_bot->command->lowToNr);
			give_value_to_output(root, a_bot->command->lowToNr, a_bot->low);
			a_bot->low = -1;
		}
		if(a_bot->command->targetTypeHigh == Output) {
			printf("HIGH to %d output %d\n", a_bot->high, a_bot->command->highToNr);
			give_value_to_output(root, a_bot->command->highToNr, a_bot->high);
			a_bot->high = -1;
		}
	}
}

void add_command(Bot *root, int from_bot_nr, Target lowTarget, int low_nr, Target highTarget, int high_nr) {
	Bot *nbot = find_bot(root, from_bot_nr);
	if(nbot == NULL) {
		nbot = create_new_bot(from_bot_nr, -1);
		Command *cmd = (Command *)malloc(sizeof(Command));
		cmd->lowToNr = low_nr;
		cmd->targetTypeLow = lowTarget;
		cmd->highToNr = high_nr;
		cmd->targetTypeHigh = highTarget;
		nbot->command = cmd;
		add_bot(root, nbot);
	}
	else {
		Command *cmd = (Command *)malloc(sizeof(Command));
		cmd->lowToNr = low_nr;
		cmd->targetTypeLow = lowTarget;
		cmd->highToNr = high_nr;
		cmd->targetTypeHigh = highTarget;
		nbot->command = cmd;
	}
}

Bot *add_value_to_bot(Bot *root, int bot_nr, int value) {
	Bot *target_bot = find_bot(root, bot_nr);
	if(target_bot != NULL) { /* Bot exists */
		printf("Add %d - %d\n", target_bot->nr, value);
		if(value > target_bot->high) {
			target_bot->low = target_bot->low > target_bot->high ? target_bot->low : target_bot->high;
			target_bot->high = value;
		}
		else {
			target_bot->high = target_bot->low > target_bot->high ? target_bot->low : target_bot->high;
			target_bot->low = value;
		}
	}
	else {
		target_bot = create_new_bot(bot_nr, value);
		printf("Add2 %d - %d\n", target_bot->nr, value);
		root = add_bot(root, target_bot);
	}
	return root;
}

Bot *handle_input(Bot *root, const char *line) {
	int bot_nr;
	int value;
	Bot *list = root;
	
	sscanf(line + 6, "%d", &value);
	int i;
	for(i = mystrlen(line); *(line + i) != ' '; i--);
	sscanf(line + i, "%d", &bot_nr);

	list = add_value_to_bot(list, bot_nr, value);	
	return list;
}

Bot *handle_command(Bot *root, const char *line) {
	/* bot 2 gives low to bot 1 and high to bot 0 */
	int fromNr;
	int lowToNr;
	Target lowTarget;
	int highToNr;
	Target highTarget;

	int pos = 4;
	char num_str[8];
	int i; 
	for(i = 0; isdigit(*(line + pos)); pos++, i++) {
		num_str[i] = *(line + pos);
	}
	num_str[i] = '\0';
	fromNr = atoi(num_str);
	
	pos += 6;
	pos += 4;
	pos += 4;
	
	lowTarget = startsWith(line + pos, "bot") ? eBot : Output;
	for(; !isdigit(*(line + pos)); pos++);
	sscanf(line + pos, "%d", &lowToNr);
	for(; *(line + pos) != ' '; pos++);
	pos += 5;
	pos += 5;
	pos += 3;
	
	highTarget = startsWith(line + pos, "bot") ? eBot : Output;
	for(; !isdigit(*(line + pos)); pos++);
	sscanf(line + pos, "%d", &highToNr);

	if(root == NULL) {
		root = create_new_bot(fromNr, -1);
	}
	add_command(root, fromNr, lowTarget, lowToNr, highTarget, highToNr);
	return root;
}

int main(int argc, char **argv)
{
    FILE *fp = fopen(*(argv + 1), "r");
    if(!fp) {
        fprintf(stderr, "FAIL!\n");
        exit(-1);
    }
	fseek(fp, 0L, SEEK_END);
	int size = ftell(fp);
	fseek(fp, 0L, SEEK_SET);
	char *buf = (char*)calloc(size + 1, sizeof(char));
	
	if(fread(buf, sizeof(char), size, fp) != size) {
		fprintf(stderr, "FAIL to read!\n");
		fclose(fp);
		exit(-1);
	}

	char *start = buf;
	char *line;
	Bot *bots = NULL;
	while(*buf && (line = mystrsep(&buf, '\n'))) {
		switch(*line) {
			case 'v':
				bots = handle_input(bots, line);
				break;
			case 'b': 
				bots = handle_command(bots, line);
				break;
			default: 
				break;
		}
	}
	buf = start;
	for(Bot *bot = bots; bot != NULL; bot = bot->next) {
		run_command(bots, bot);
	}
	printf("\nDUMP goes here\n***********************\n\n");
	dump_bot(bots);

	while(bots->next != NULL) {
		Bot *tail = bots->next;
		if(bots->command != NULL) {
			free(bots->command);
		}
		free(bots);
		bots = tail; 
	}
	free(bots); 
	free(buf);
	return 0;
}
