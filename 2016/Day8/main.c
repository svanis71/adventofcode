#include <stdio.h>
#include <stdlib.h>
#include "mystring.h"

void copy_screen(int src[][6], int dest[][6]) {
	for(int c = 0; c < 50; c++) 
		for(int r = 0; r < 6; r++)
			dest[c][r] = src[c][r];
}

void rotate_col(int screen[][6], int pos, int steps) {
	int tmp_screen[50][6];
	copy_screen(screen, tmp_screen);
	for(int r = 0; r < 6; r++) {
		int new_pos = (r + steps) % 6;
		tmp_screen[pos][new_pos] = screen[pos][r];
	}
	copy_screen(tmp_screen, screen);
}

void rotate_row(int screen[][6], int pos, int steps) {
	int tmp_screen[50][6];
	copy_screen(screen, tmp_screen);
	for(int c = 0; c < 50; c++) {
		int new_pos = (c + steps) % 50;
		tmp_screen[new_pos][pos] = screen[c][pos];
	}
	copy_screen(tmp_screen, screen);
}

void rect(int screen[][6], int cols, int rows) {
	for(int c = 0; c < cols; c++)
		for(int r = 0; r < rows; r++)
			screen[c][r] = 1;
}

int read_int(const char *buf) {
	char *input = (char*)calloc(5, sizeof(char));
	for(int i = 0; *(buf + i) && isdigit(*(buf + i)); i++) {
		*(input + i) = *(buf + i);
	}
	int val = atoi(input);
	free(input);
	return val;
}

int print_screen(int screen[][6]) {
	int cnt = 0;
	for(int r = 0; r < 6; r++) {
		for(int c = 0; c < 50; c++) {
			if(screen[c][r] == 1)
				cnt++;
			printf("%c", screen[c][r] == 1 ? '#' : ' ');
		}
		printf("\n");
	}
	return cnt;
}

int main(int argc, char **argv) {
    FILE *fp = fopen(*(argv + 1), "r");
    if(!fp) {
        fprintf(stderr, "FAIL!\n");
        exit(-1);
    }
    int screen[50][6];
    char *buf = (char *)calloc(255, sizeof(char));
	
	for(int r = 0; r < 6; r++) {
		for(int c = 0; c < 50; c++) {
			screen[c][r] = 0;
		}
	}
	
    while(fgets(buf, 255, fp)) {
        if(strnequal(buf, "rect", 4)) {
			char *p2 = buf + 4;
			char *p1 = mystrsep(&p2, 'x');
			int cols = atoi(p1);
			int rows = atoi(p2);
			rect(screen, cols, rows);
			p2 = buf;
        }
        if(strnequal(buf, "rotate", 6)) {
			char dir = 'r';
			char *tmp = buf + 7;
			if(strnequal(tmp, "column", 6)) {
				dir = 'c';
				tmp += 9;
			}
			else {
				tmp += 6;
			}
			int pos = read_int(tmp);
			while(*tmp++ != 'y');
			int steps = read_int(++tmp);
			if(dir == 'c')
				rotate_col(screen, pos, steps);
			else
				rotate_row(screen, pos, steps);
			tmp = buf;
        }
    }

	int on_cnt = print_screen(screen);
	printf("%d pixels are on.\n", on_cnt);
	
    free(buf);
    fclose(fp);
    return 0;
}