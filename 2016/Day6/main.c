#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROWS 26

int main(int argc, char **argv)
{
	int cols = 8;
	int map[cols][ROWS];
	
	FILE *fp = fopen(*(argv + 1), "r");
	if(!fp) {
		fprintf(stdout, "Fail!\n");
		exit(-1);
	}
	
	char *buf = (char *)calloc(255, sizeof(char));
	char *buf_part2 = (char *)calloc(cols + 1, sizeof(char));

	for(int c = 0; c < cols; c++) {
		for(int r = 0; r < 26; r++) {
			map[c][r] = 0;
		}
	}
	while(fgets(buf, 255, fp) != NULL) {
		for(int i = 0; *(buf + i) && *(buf + i) != '\r' && *(buf + i) != '\n'; i++) {
			int c = *(buf + i) - 'a';
			map[i][c] += 1;
		}
		memset(buf, '\0', 255);
	}
	
	int max_val = 0;
	int max_row = 0;
	int min_val = 0;
	int min_row = 0;
	
	for(int col = 0; col < cols; col++) {
		int max = (int)'a';
		max_val = 0;
		max_row = 0;
		min_val = 99;
		min_row = 0;
	
		for(int row = 0; row < ROWS; row++) {
			if(map[col][row] > max_val) {
				max_val = map[col][row];
				max_row = row;
			}
			if(map[col][row] < min_val) {
				min_val = map[col][row];
				min_row = row;
			}
			*(buf + col) = 'a' + (char)max_row;
			*(buf_part2 + col) = 'a' + (char)min_row;
		}
	}

	printf("%s\n%s\n", buf, buf_part2);
	free(buf);
	free(buf_part2);
	fclose(fp);
	return 0;
}
