#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct elf {
	struct elf *next;
	struct elf *prev;
	int nr;
}ELF;

int part1(int size) {
	char *elfs = (char *)calloc(size, sizeof(char));
	memset(elfs, '1', size);
	int stop = 0;
	int cnt = 0;
	int next = 0;
	while(!stop) {
		for(next = (cnt + 1) % size; next != cnt && *(elfs + next) != '1'; next = (next + 1) % size);
		if(next == cnt)
			stop = 1;
		else {
			*(elfs + next) = '0';
			for(cnt = (next + 1) % size; *(elfs + cnt) != '1'; cnt = (cnt + 1) % size);
		}
	}
	free(elfs);
	return cnt + 1;
}

ELF *create_elf(int nr) {
	ELF *alv = (ELF *)malloc(sizeof(ELF));
	alv->nr = nr;
	alv->next = NULL;
	alv->prev = NULL;
	return alv;
}

int part2(int size) {
	ELF *left = NULL;
	ELF *right = NULL;
	ELF *tail = NULL;

	for(int i = 0; i < size; i++) {
		ELF *itm = create_elf(i+1);
		if(left == NULL) {
			left = itm;
			tail = left;
			tail->next = left;
			tail->prev = left;
		}
		else {
			itm->prev = tail;
			itm->prev->next = itm;
			itm->next = left;
			tail = itm;
			left->prev = tail;
			if(i == size / 2) {
				right = itm;
			}
		}
	}

	int cnt = size;
	while(cnt > 1) {
/*		printf("size %d\t (", cnt);
		for(ELF *l = tail->next; l != tail; l = l->next) {
			printf("%d ", l->nr);
		}
		printf("%d)\n", tail->nr);

		printf("|left-----|right----|\n");
		printf("|%9d|%9d|\n", left->nr, right->nr);
		printf("|---------|---------|\n");*/
		ELF *t = right;
		right->prev->next = right->next;
		right->next->prev = right->prev;
		if(t == tail)
			tail = tail->prev;
		if(cnt % 2 == 1)
			right = right->next->next;
		else
			right = right->next;
		free(t);
		left = left->next;
		cnt--;
	}
	int ret = left->nr;
	free(left);
	return ret;
}

int main(int argc, char **argv)
{
	int size = atoi(*(argv + 1));
	printf("Part 1: Last elf is number %d\n", part1(size));
	printf("Part 2: Last elf is number %d\n", part2(size));
	return 0;
}

