/*
 -------------------------------------
 File:    myrecord.c
 Project: fedo0350_a04
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-02-07
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "myrecord.h"

#define MAX_LINE 100

char letter_grade(float s) {

	char lettergrade = 'F';
	if (50 <= s && s < 60)
		lettergrade = 'D';
	else if (60 <= s && s < 70)
		lettergrade = 'C';
	else if (70 <= s && s < 80)
		lettergrade = 'B';
	else if (80 <= s && s < 90)
		lettergrade = 'A';
	else if (90 <= s && s < 100)
		lettergrade = 'S';

	return lettergrade;

}

int import_data(RECORD dataset[], char *filename) {

	FILE *fp = fopen("marks.txt", "r");

	char delimiters[] = " ,\n\r";
	char line[100];
	int i = 0;
	char *token = NULL;
	while (fgets(line, sizeof(line), fp) != NULL) {
		token = (char*) strtok(line, delimiters);
		strcpy(dataset[i].name, token);
		token = (char*) strtok(NULL, delimiters);
		dataset[i].score = atof(token);
		i++;
	}

	fclose(fp);
	return i;
}

STATS get_stats(RECORD dataset[], int n) {

	float sorted[n];
	float median = 0.0;
	STATS stats = { };
	if (n < 1)
		return stats;

	float mean = 0;
	float stddev = 0;

	int i = 0;

	for (i = 0; i < n; i++) {
		mean += dataset[i].score;
	}

	mean /= n;

	for (i = 0; i < n; i++) {
		stddev += (dataset[i].score - mean) * (dataset[i].score - mean);
	}

	int count = n;
	stddev = sqrt(stddev / count);

	stats.mean = mean;
	stats.stddev = stddev;
	stats.count = count;

	for (int i = 0; i < n; i++)
		sorted[i] = dataset[i].score;

	float swapper = 0.0;
	int h, j, k;
	for (h = 0; h < n; ++h) {
		k = h;
		for (j = h + 1; j < n; ++j) {
			if (sorted[j] < sorted[k]) {
				k = j;
			}
		}
		if (h != k) {

			swapper = sorted[k];
			sorted[k] = sorted[h];
			sorted[h] = swapper;
		}
	}

	if (n % 2 != 0)
		median = sorted[n / 2];
	else
		median = (sorted[n / 2 - 1] + sorted[n / 2]) / 2;

	stats.median = median;

	return stats;
}

STATS report_data(RECORD dataset[], int n, char *filename) {
	STATS stats = { };
	if (n < 1)
		return stats;

	FILE *fp = fopen("report.txt", "w");
	if (fp == NULL) {
		perror("error");
		return stats;
	}
	int i = 0;
	for (i = 0; i < n; i++) {
		fprintf(fp, "%s,%c\n", dataset[i].name, letter_grade(dataset[i].score));
	}
	fclose(fp);

	return get_stats(dataset, n);
}
