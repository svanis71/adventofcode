#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void chomp(char *str)
{
  for(int i = 0; *(str + i); i++) {
    if(*(str + i) == '\r' || *(str + i) == '\n') {
      *(str + i) = '\0';
    }
  }
}

int checkInsideSquareBrackets1(const char *buf) {
	int valid = 1;
	for(int i = 0; *(buf + i) && valid; i++) {
		if(*(buf + i) == '[') {
			while(*(buf + i + 3) != ']') {
				if(*(buf + i) != *(buf + i + 1) && *(buf + i) == *(buf + i + 3) && *(buf + i + 1) == *(buf + i + 2)) {
					valid = 0;
				}
				i++;
			}
		}
	}
	return valid;
}

int partOne(const char *buf) {
	int valid = 0;

	if(checkInsideSquareBrackets1(buf)) {
		for(int i = 0; *(buf + i) && !valid; i++) {
			if(*(buf + i) != *(buf + i + 1) && *(buf + i) == *(buf + i + 3) && *(buf + i + 1) == *(buf + i + 2)) {
				valid = 1;
			}
		}
	}
	return valid;
}

int partTwo(const char *buf) {
	int valid = 0;
	
	for(int i = 0; *(buf + i) && !valid; i++) {
		if(*(buf + i) == '[') {
			while(*(buf + i) != ']')
				i++;
		}
		int j = 0;		
		if(*(buf + i) != *(buf + i + 1) && *(buf + i) == *(buf + i + 2)) {
			while(*(buf + j)) {
				while(*(buf + j) && *(buf + j) != '[')
					j++;
				for(; *(buf + j) && *(buf + j) != ']' && !valid; j++) {
					if(*(buf + j) == *(buf + j + 2) && *(buf + j) == *(buf + i + 1) && *(buf + j + 1) == *(buf + i)) {
						valid = 1;
					}
				}
				j++;
			}
		}
	}
	return valid;
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(*(argv + 1), "r");
	
	if(!fp) {
		fprintf(stderr, "FAIL!\n");
		exit(-1);
	}
	
	char *buf = (char *)calloc(255, 1);
	int cnt1 = 0;
	int cnt2 = 0;
    
	while(fgets(buf, 255, fp)) {
		chomp(buf);
		cnt1 = cnt1 + partOne(buf);
		cnt2 = cnt2 + partTwo(buf);
		memset(buf, '\0', 255);
	}
	printf("Part 1: %d\n", cnt1);
	printf("Part 2: %d\n", cnt2);

	fclose(fp);
	free(buf);
	
	return 0;
}
