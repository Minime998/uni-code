/*
 -------------------------------------
 File:    myrecord_sllist.h
 Project: fedo0350_a03
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-01-31
 -------------------------------------
 */

#ifndef SLLIST_H
#define SLLIST_H

typedef struct {
	char name[40];
	float score;
} RECORD;

typedef struct node {
	RECORD data;
	struct node *next;
} NODE;

typedef struct sllist {
	int length;
	NODE *start;
} SLLIST;

void display(SLLIST *sllistp);

NODE* search(SLLIST *sllistp, char *name);

void insert(SLLIST *sllistp, char *name, float score);

int delete(SLLIST *sllistp, char *name);

void clean(SLLIST *sllistp);

// The following are adapted/modified from A4Q2 for A5Q1
typedef struct {
	int count;
	float mean;
	float stddev;
	float median;
} STATS;

char letter_grade(float score);
int import_data(SLLIST *sllistp, char *infilename);
STATS report_data(SLLIST *sllistp, char *outfilename);

#endif
