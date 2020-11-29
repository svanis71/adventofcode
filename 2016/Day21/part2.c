#include <stdio.h>
#include <stdlib.h>
#include "mystring.h"

typedef struct __cmd__ {
	char command_line[40];
	struct __cmd__ *next;
	struct __cmd__ *prev;
} Command;

int find_ch(const char *s, char c) {
	int idx = 0;
	while(*(s + idx) && *(s + idx) != c) idx++;
	return *(s + idx) == c ? idx : -1;
}

int find_digit(const char *s) {
	int idx = 0;
	while(*(s + idx) && !isdigit(*(s + idx))) idx++;
	return isdigit(*(s + idx)) ? idx : -1;
}

int get_number(const char *s) {
	int i = 0;
	while(*(s + i) && (*(s + i) < '0' || *(s + i) > '9')) i++;
	return *(s + i) - '0';
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(*(argv + 1), "r");
    if(!fp) {
        fprintf(stderr, "FAIL!\n");
        exit(-1);
    }
	char *line = (char*)calloc(80, sizeof(char));

	Command *list = NULL;
	int r = 1;
	while((line = fgets(line, 80, fp)) != NULL) {
		chomp(line);
		/* Commands:
		 *  swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
			swap letter d with letter b swaps the positions of d and b: edcba.
			reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
			rotate left 1 step shifts all letters left one position, causi(ng the first letter to wrap to the end of the string: bcdea.
			move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
			move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
			rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
			rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.
		 */
		if(*line == 'r') {
			if(*(line + 1) == 'e') {
				int p1 = get_number(line);
				int p2 = get_number(line + mystrlen(line) - 1);
				sprintf(line, "reverse positions %d through %d", p1, p2);
			}
			else {
				if(*(line + 7) == 'l') {
					int n = get_number(line);
					sprintf(line, "rotate right %d", n);
				}
				else if(*(line + 7) == 'r') {
					int n = get_number(line);
					sprintf(line, "rotate left %d", n);
				}
				else {
					char ch = *(line + mystrlen(line) - 1);
/*					int pos = mystrlen(data);
					while(*(data + pos) != ch) pos--;
					int n = len - pos + 1;*/
					sprintf(line, "rotate xbased on position of letter %c", ch); /*n > 4 ? n + 1 : n);*/
				}
			}
		}
		if(*line == 'm') {
			int p1 = get_number(line);
			int p2 = get_number(line + mystrlen(line) - 1);
			sprintf(line, "move position %d to position %d", p2, p1);
		}
		if(*line == 's') {
			if(*(line + 5) == 'p') {
				int p1 = get_number(line);
				int p2 = get_number(line + mystrlen(line) - 1);
				sprintf(line, "swap position %d with position %d", p2, p1);
			}
			else {
				char c1 = *(line + 12);
				char c2 = *(line + mystrlen(line) - 1);
				sprintf(line, "swap letter %c with letter %c", c2, c1);
			}
		}

		printf("%d: %s\n", r++, line);
		Command *item = (Command *)malloc(sizeof(Command));
		item->next = NULL;
		item->prev = NULL;
/*		item->command_line = (char *)calloc(mystrlen(line) + 1, sizeof(char));*/
		mystrcpy(item->command_line, line);
		if(list == NULL)
			list = item;
		else {
			Command *l = list;
			while(l->next != NULL) {
				l = l->next;
			}
			item->prev = l;
			l->next = item;
		}
	}
	free(line);
	fclose(fp);

	fp = fopen("in2.txt", "w");
	Command *itm = list;
	while(itm->next != NULL) {
		itm = itm->next;
	}
	while(itm->prev != NULL) {
		fprintf(fp, "%s\n", itm->command_line);
		Command *t = itm;
		itm = itm->prev;
		free(t);
	}
	fprintf(fp, "%s\n", list->command_line);
	free(list);
	fclose(fp);


	return 0;
}
