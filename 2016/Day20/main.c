#include <stdio.h>
#include <stdlib.h>
#include "mystring.h"

struct item {
	unsigned int min;
	unsigned int max;
	struct item *next;
	struct item *prev;
};

struct item *insert_item(struct item *head, struct item *new_item) {
	if(head->min > new_item->min) {
		new_item->next = head;
		head->prev = new_item;
		return new_item;
	}

	struct item *list = head;
	while(list != NULL) {
		if(new_item->min < list->min) {
			struct item *p = list->prev;
			new_item->next = list;
			new_item->prev = list->prev;
			list->prev->next = new_item;
			list->prev = new_item;
			break;
		}
		else if(list->next == NULL) {
			new_item->prev = list;
			list->next = new_item;
			break;
		}
		list = list->next;
	}
	return head;
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
	char *line;
	struct item *blacklist = NULL;

	if(fread(buf, sizeof(char), size, fp) != size) {
		fprintf(stderr, "FAIL to read!\n");
		fclose(fp);
		exit(-1);
	}
	int i = 0;
	for(; *buf && (line = mystrsep(&buf, '\n')); i+=2) {
		/* 1224-4000 */
		unsigned int i1, i2;
		char *i1str = mystrsep(&line, '-');
		char *s;
		i1 = strtoul(i1str, &s, 10);
		i2 = strtoul(line, &s, 10);
		struct item *n = (struct item *)malloc(sizeof(struct item));
		n->min = i1;
		n->max = i2;
		n->next = NULL;
		n->prev = NULL;
		if(blacklist == NULL) {
			blacklist = n;
		}
		else {
			blacklist = insert_item(blacklist, n);
		}
	}
	unsigned int min = blacklist->max;
	unsigned int a1;
	unsigned int count = 0UL;
	unsigned int latest = 0UL;
	unsigned int umax = 4294967295UL;

	int found = 0;
	for(struct item *l = blacklist; l != NULL; l = l->next) {
		struct item *peek = l->next;
		if(l->max > latest)
			latest = l->max;

		if(peek != NULL) {
			for(unsigned int c = latest + 1; c < peek->min && c > latest; c++)  {
				count = count + 1UL;
			}
			if(min + 1 < l->next->min) {
				a1 = min + 1U;
			}
			else {
				min = peek->max > l->max ? peek->max : l->max;
			}
		}
	}
	unsigned int diff = umax - latest;
	printf("umax =\t%u\nlate =\t%u\ncnt =\t%u\nrest =\t%u\n", umax, latest, count, diff);
	unsigned int total = count + diff;
	printf("valid =\t%u\n", total);
	printf("\nMin is %u\n", a1);

	while(blacklist->next != NULL) {
		struct item *tail = blacklist->next;
		free(blacklist);
		blacklist = tail;
	}
	free(blacklist);

	char *t;
	char s[15];
	sprintf(s, "%u", umax);
	unsigned int ul = strtoul(s, &t, 10);
	printf("%u\n", ul);

	return 0;
}
