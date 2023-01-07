/*
 -------------------------------------
 File:    matrix.c
 Project: fedo0350_a02
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-01-24
 -------------------------------------
 */

#include<stdio.h>
#include "matrix.h"

void display_vector(int *v, int n) {
	int *p = v, i, j;
	for (i = 0; i < n; i++) {
		printf("%-4d", *p++);
	}
	printf("\n");
}

void display_matrix(int *m, int n) {
	int *p = m, i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++)
			printf("%4d", *p++);
		printf("\n");
	}
}

int vsum(int *v, int n) {
	int total = 0;
	for (int i = 0; i < n; i++) {
		total += *(v + i);
	}
	return total;
}

int msum(int *m, int n) {
	double total = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			total += *(m + i * n + j);
		}
	}
	return total;
}

void transpose_matrix(int *m1, int *m2, int n) {

	int i, j;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			*(m2 + j * n + i) = *(m1 + i * n + j);
}

void multiply_matrix(int *m1, int *m2, int *m3, int n) {
	int i, j, k, sum;
	for (i = 0; i < n; i++) {
		for (j = 0; j < 4; j++) {
			sum = 0;
			for (k = 0; k < n; k++) {
				sum += *(m1 + i * n + k) * (*(m2 + k * n + j));
			}
			*(m3 + i * n + j) = sum;
		}
	}
}

void multiply_vector(int *m, int *vin, int *vout, int n) {
	int i, j;
	int sum = 0; //why?

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			sum += *(vin + j) * (*(m + i * n + j));
		}
		*(vout + i) = sum;
		sum = 0;
	}
}
