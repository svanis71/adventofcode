#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
	int len = strlen(*(argv + 1));
	char *input = (char *)calloc(len + 1, sizeof(char));
	int disk_size = atoi(*(argv + 2));
	strcpy(input, *(argv + 1));

	while(len < disk_size) {
		int new_len = len * 2 + 1;
		input = (char *)realloc(input, new_len);
		*(input + len) = '0';
		for(int i = 0, j = len - 1; i < len; i++, j--) {
			*(input + len + i + 1) = (~(*(input + j) - '0') & 0x1) + '0';
		}
		len = new_len;
	}
	*(input + disk_size) = '\0';

	int cslen = disk_size / 2;
	while(cslen % 2 == 0) {
		int i = 0;
		for(i = 0, cslen = 0; *(input + i) != '\0'; i += 2, cslen++) {
			*(input + cslen) = (*(input + i) == *(input + i + 1)) + '0';
		}
		*(input + cslen) = '\0';
	}

	puts(input);
	free(input);
	return 0;
}
