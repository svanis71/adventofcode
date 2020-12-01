#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TRAP '^'
#define SAFE '.'

int left_trap(const char *s, int curr) {
	return curr != 0 && *(s + curr - 1) == TRAP;
}

int center_trap(const char *s, int curr) {
	return *(s + curr) == TRAP;
}

int right_trap(const char *s, int curr) {
	return *(s + curr + 1) != '\0' && *(s + curr + 1) == TRAP;
}

int safe_count(const char *line) {
	int cnt = 0;
	for(int i = 0; *(line + i) != '\0'; i++)
		if(*(line + i) == '.')
			cnt++;
	return cnt;
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(*(argv + 1), "r");
	int rows_to_count = atoi(*(argv + 2));

	if(!fp) {
		fprintf(stderr, "Fail :-(\n");
		exit(-1);
	}
	fseek(fp, 0L, SEEK_END);
	int size = ftell(fp);
	fseek(fp, 0L, SEEK_SET);
	char *prev = (char*)calloc(size + 1, sizeof(char));
	if(fread(prev, sizeof(char), size, fp) != size) {
		fprintf(stderr, "FAIL to read!\n");
		fclose(fp);
		exit(-1);
	}
	fclose(fp);

	int safe_cnt = safe_count(prev);
	char *next = (char*)calloc(size + 1, sizeof(char));

	for(int r = 0; r < rows_to_count - 1; r++) {
		for(int c = 0; *(prev + c) != '\0'; c++) {
			if(*(prev + c) == '\r' || *(prev + c) == '\n') {
				*(prev + c) = '\0';
				continue;
			}
			int left = left_trap(prev, c);
			int center = center_trap(prev, c);
			int right = right_trap(prev, c);
			int rule1 = left && center && !right;
			int rule2 = !left && center && right;
			int rule3 = left && !center && !right;
			int rule4 = !left && !center && right;
			*(next + c) = (rule1 || rule2 || rule3 || rule4) ? TRAP : SAFE;
		}
		safe_cnt += safe_count(next);
		strcpy(prev, next);
	}
	fprintf(stdout, "Safe count: %d\n", safe_cnt);

	free(prev);
	free(next);
	return 0;
}
