/*
 -------------------------------------
 File:    myword.c
 Project: fedo0350_a03
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-01-31
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include "mystring.h"
#include "myword.h"

int process_word(char *infilename, WORDINFO *wip) {
	const char delimiters[] = " .,;:!()&?-\n\t\r\"\'";
	char line[MAX_LINE_LEN];
	char *word_token = NULL;
	int j;
	FILE *fp = fopen("textdata.txt", "r");
	while (fgets(line, MAX_LINE_LEN, fp) != NULL) {
		wip->line_count++;
		lower_case(line);
		trim(line);
		word_token = (char*) strtok(line, delimiters);
		while (word_token != NULL) {
			int i = 0;
			for (j = 0; j < wip->distinct_word_count; j++) {
				if (strcmp(word_token, wip->word_array[j].word) == 0) {
					wip->word_array[j].frequency += 1;
					wip->word_count++;
					i = 1;
				}
			}
			if (i == 0) {

				strcpy(wip->word_array[wip->distinct_word_count].word,
						word_token);
				wip->word_array[wip->distinct_word_count].frequency = 1;
				wip->distinct_word_count++;
				wip->word_count++;

			}

			word_token = (char*) strtok(NULL, delimiters);
		}
	}
	fclose(fp);
}

int save_to_file(char *outfilename, WORDINFO *wip) {
	FILE *fp = fopen("results.txt", "w");
	if (fp == NULL) {
		perror("file opening error");
		return 1;
	}
	fprintf(fp, "%s:%d\n", "line count", wip->line_count);
	fprintf(fp, "%s:%d\n", "word count", wip->word_count);
	fprintf(fp, "%s:%d\n", "distinct word count", wip->distinct_word_count);
	int i;
	for (i = 0; i < wip->distinct_word_count; i++) {
		fprintf(fp, "%s:%d\n", wip->word_array[i].word,
				wip->word_array[i].frequency);
	}
	fclose(fp);
	return 0;
}
