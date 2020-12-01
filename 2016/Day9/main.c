#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include "mystring.h"

#define CHUNK_SIZE 512000

void part1(char *buf) {
	char *walker = buf;
	int allocated_bytes = mystrlen(buf) + 1 + CHUNK_SIZE;
	char *decompressed = (char*)calloc(allocated_bytes, sizeof(char));
	
	while(*walker) {
		while(*walker <= ' ') {
			walker++;
			continue;
		}
		int curr_len = mystrlen(decompressed);
		if(*walker == '(') {
			// Marker
			walker++; // skip (
			char *nbytes = mystrsep(&walker, 'x');
			int bytes = atoi(nbytes);
			char *reps = mystrsep(&walker, ')');
			int repetitions = atoi(reps);
			char *copy = (char *)calloc(bytes * repetitions + 1, sizeof(char));
			int next_size = curr_len + (repetitions * bytes);
			while(next_size >= allocated_bytes) {
				allocated_bytes += CHUNK_SIZE;
				decompressed = (char *)realloc(decompressed, allocated_bytes);
			}
			copy_characters(copy, walker, bytes);
			for(int i = 0; i < repetitions; i++)
				mystrcat(decompressed, copy);
			walker += bytes;
		}
		else {
			if(curr_len + 1 >= allocated_bytes) {
				allocated_bytes += CHUNK_SIZE;
				decompressed = (char *)realloc(decompressed, allocated_bytes);				
			}
			*(decompressed + curr_len) =  *walker++;
		}		
	}
	walker = buf;
	printf("%s\nDecompressed size is: %d\n", decompressed, mystrlen(decompressed));
	free(decompressed);
}

long part2(char *buf) {
	char *walker = buf;
	long len = 0;

	if(!(*buf)) {
		return len;
	}

	if(*walker != '(') {
		for(;*walker && *walker != '('; walker++) {
			len++;
		}
	}
	
	while(*walker == '(') {
		// Marker
		walker++; // skip (
		char *nbytes = mystrsep(&walker, 'x');
		int bytes = atoi(nbytes);
		char *reps = walker;
		while(*walker++ != ')');
		*(walker - 1) = '\0';
		int repetitions = atoi(reps);
		char *tmp = (char *)calloc(bytes + 1, sizeof(char));
		copy_characters(tmp, walker, bytes);
		len += (repetitions * part2(tmp));
		walker += bytes;
		free(tmp);
	}
	
	return len + part2(walker);
}

int main(int argc, char **argv) {
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
	
/*	part1(buf);*/
	printf("Len is %ld\n", part2(buf));
	free(buf);
	return 0;
}
