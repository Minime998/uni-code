/*
-------------------------------------
File:    mysort.h
Project: fedo0350_a04
file description
-------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Version  2022-02-07
-------------------------------------
 */
#ifndef MYSORT_H
#define MYSORT_H 

typedef enum {
    false = 0, true = 1
} BOOLEAN;
BOOLEAN is_sorted(int *a, int left, int right);
void select_sort(int *a, int left, int right);
void quick_sort(int *a, int left, int right);

#endif
