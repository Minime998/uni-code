/*
 -------------------------------------
 File:    mysort.c
 Project: fedo0350_a04
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-02-07
 -------------------------------------
 */

#include "mysort.h"
#include <stdio.h>

BOOLEAN is_sorted(int *a, int left, int right) {
	int counter = 0;
	left = a[counter];
	right = a[counter + 1];
	BOOLEAN check = true;
	while (check == true && counter < sizeof(a)) {
		if (left > right) {
			check = false;
		}
		counter++;
	}
	return check;
}

void select_sort(int *a, int left, int right) {
	int swapper = 0;
	int i, j, k;
	for (i = 0; i < sizeof(a); ++i) {
		k = i;
		for (j = i + 1; j < sizeof(a); ++j) {
			if (*(a + j) < *(a + k)) {
				k = j;
			}
		}
		if (i != k) {
			swapper = *(a + k);
			*(a + k) = *(a + i);
			*(a + i) = swapper;
		}
	}
}

void quick_sort(int *a, int left, int right) {

	int key, i, j, k, swap;
	if (left < right) {
		key = *(a + left);
		i = left + 1;
		j = right;
		while (i <= j) {
			while (i <= right && *(a + i) <= key)
				i++;
			while (j >= left && *(a + j) > key)
				j--;
			if (i < j) {
				swap = *(a + i);
				*(a + i) = *(a + j);
				*(a + j) = swap;
			}
		}

		swap = *(a + left);
		*(a + left) = *(a + j);
		*(a + j) = swap;
		quick_sort(a, left, j - 1);
		quick_sort(a, j + 1, right);
	}

}
