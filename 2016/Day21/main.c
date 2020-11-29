#include <stdio.h>
#include <stdlib.h>
#include "mystring.h"

#define INPUT_STR "abcdefgh"
#define INPUT_STR2 "fbgdceah"

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

void process_swap(const char *swap_cmd, char **str) {
	int p1 = 0, p2 = 0;
	if(*swap_cmd == 'p') {
		int dig_pos = find_digit(swap_cmd);
		p1 = get_number(swap_cmd + dig_pos);
		dig_pos = find_digit(swap_cmd + dig_pos + 1);
		p2 = get_number(swap_cmd + dig_pos);
	}
	else {
		char ch = *(swap_cmd + 7);
		p1 = find_ch(*str, ch);
		ch = *(swap_cmd + 21);
		p2 = find_ch(*str, ch);
	}
	char t = *(*str + p1);
	*(*str + p1) = *(*str + p2);
	*(*str + p2) = t;
}

void process_reverse(const char *cmd, char **str) {
	/* 0 through 4 */
	int start = *cmd - '0';
	int end = get_number(cmd + start + 1);
	for(; start < end; start++, end--) {
		char t = *(*str + start);
		*(*str + start) = *(*str + end);
		*(*str + end) = t;
	}
}

void process_rotate(const char *cmd, char **str) {

	if(*cmd == 'b') {
		/* rotate based on position of letter b */
		/* Hitta positionen rotera 1+positionen
		 * och om positionen >= 4 rotera en xtra */
		char ch = *(cmd + mystrlen(cmd) - 1);
		int pos = find_ch(*str, ch);
		int rots = 1 + pos + (pos >= 4 ? 1 : 0);
		char *new_cmd = (char *)calloc(15, sizeof(char));
		sprintf(new_cmd, "right %d", rots);
		process_rotate(new_cmd, str);
		free(new_cmd);
	}
	else if(*cmd == 'x') {
		char ch = *(cmd + mystrlen(cmd) - 1);
		int pos = find_ch(*str, ch);
		int rots = 0;
		char *new_cmd = (char *)calloc(15, sizeof(char));
		switch(pos) {
			case 0:
				rots = 9;
				break;
			case 1:
				rots = 7;
				break;
			case 2:
				rots = 2;
				break;
			case 3:
				rots = 6;
				break;
			case 4:
				rots = 1;
				break;
			case 5:
				rots = 5;
				break;
			case 6:
				rots = 8;
				break;
			case 7:
				rots = 4;
				break;
		}
		sprintf(new_cmd, "right %d", rots);
		process_rotate(new_cmd, str);
		free(new_cmd);
	}
	else if (*cmd == 'l' || *cmd == 'r') {
		int dir = -1;
		if(startsWith(cmd, "right") == 1)
			dir = 1;
		int n = get_number(cmd);
		int len = mystrlen(*str);
		char *copy = (char *)calloc(len + 1, sizeof(char));
		for(int i = 0; i < len; i++) {
			if(dir < 0) {
				int index = i >= n ? i - n : len - n + i;
				*(copy + index)  = *(*str + i);
			}
			else {
				int index = (i + n) % len;
				*(copy + index)  = *(*str + i);
			}
		}
		mystrcpy(*str, copy);
		free(copy);
	}
}

void process_move(const char *cmd, char **str) {
	int from = get_number(cmd);
	int to = get_number(cmd + 1);
	char t = *(*str + from);
	if(from < to) {
		for(int i = from + 1; i <= to; i++) {
			*(*str + i - 1) = *(*str + i);
		}
	}
	else {
		for(int i = from; i >= to; i--) {
			*(*str + i) = *(*str + i - 1);
		}
	}
	*(*str + to) = t;
}

void handle_input(const char *line, char **data) {
	 if(*line == 's') {
		 process_swap(line + 5, data);
	 }
	 if(*line == 'r') {
		 if(*(line + 1) == 'e') {
			 process_reverse(line + mystrlen("reverse positions "), data);
		 }
		 else {
			 process_rotate(line + mystrlen("rotate "), data);
		 }
	 }
	 if(*line == 'm') {
		 process_move(line + mystrlen("move position "), data);
	 }
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(*(argv + 1), "r");
    if(!fp) {
        fprintf(stderr, "FAIL!\n");
        exit(-1);
    }
	char *line = (char*)calloc(80, sizeof(char));
	char *line2 = (char*)calloc(80, sizeof(char));

	char *data = (char *)calloc(mystrlen(INPUT_STR) + 1, sizeof(char));
	mystrcpy(data, INPUT_STR);
	char *data2 = (char *)calloc(mystrlen(INPUT_STR) + 1, sizeof(char));
	mystrcpy(data2, INPUT_STR2);

	int row = 1;
	while((line = fgets(line, 80, fp)) != NULL) {
		chomp(line);
		handle_input(line, &data);
	}
	fclose(fp);

	FILE *fp2 = fopen(*(argv + 2), "r");
    if(!fp2) {
        fprintf(stderr, "FAIL!\n");
        exit(-1);
    }
	row = 1;
	while((line2 = fgets(line2, 80, fp2)) != NULL) {
		chomp(line2);
		handle_input(line2, &data2);
	}

	printf("Password 1: %s\n", data);
	printf("Password 2: %s\n", data2);
	free(line);
	free(line2);
	free(data);
	fclose(fp2);
	return 0;
}
