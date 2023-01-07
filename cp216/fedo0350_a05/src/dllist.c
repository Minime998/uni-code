/*
 -------------------------------------
 File:    dllist.c
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
#include <stdlib.h>
#include "dllist.h"

NODE* new_node(char data) {

	NODE *np = (NODE*) malloc(sizeof(NODE));

	np->data = data;
	np->prev = NULL;
	np->next = NULL;

	return np;
}

void insert_start(DLLIST *dllistp, NODE *np) {
	if (dllistp->start == NULL) { // when the dllist is empty
		np->prev = NULL;
		np->next = NULL;
		dllistp->start = np;
		dllistp->end = np;
		dllistp->length++;
	} else { // the following linking operations to set np at start
		np->prev = NULL; // this set prev of np to NULL, as start nodenp->next = dllistp->start; // set next of np to the current start
		np->next = dllistp->start;
		dllistp->start->prev = np; // set the prev of current start to npdllistp->start = np; // set the start of the dllist to np
		dllistp->start = np;
		dllistp->length++;
	}
}

void insert_end(DLLIST *dllistp, NODE *np) {
	if (dllistp->start == NULL) { // when the dllist is empty
		np->prev = NULL;
		np->next = NULL;
		dllistp->start = np;
		dllistp->end = np;
		dllistp->length++;
	} else {
		np->next = NULL;
		np->prev = dllistp->end;
		dllistp->end->next = np;
		dllistp->end = np;
		dllistp->length++;
	}
}

void delete_start(DLLIST *dllistp) {
	NODE *np = dllistp->start;

	if (dllistp->start != NULL) {
		if (dllistp->start->next == NULL) {
			dllistp->start = NULL;
			free(dllistp->start);
			dllistp->length--;
		} else {
			dllistp->start = np->next;
			free(np);
			dllistp->start->prev = NULL;
			dllistp->length--;
		}
	}
}

void delete_end(DLLIST *dllistp) {
	NODE *np = dllistp->end;

	if (dllistp->end != NULL) {
		if (dllistp->end->prev == NULL) {
			dllistp->end = NULL;
			free(dllistp->start);
			dllistp->length--;
		} else {
			dllistp->end = np->prev;
			free(np);
			dllistp->end->next = NULL;
			dllistp->length--;
		}
	}
}

void display_forward(DLLIST *dllistp) {
	NODE *np = dllistp->start;
	while (np != NULL) {
		printf("%c", np->data);
		np = np->next;
	}
}

void display_backward(DLLIST *dllistp) {
	NODE *np = dllistp->end;
	while (np != NULL) {
		printf("%c", np->data);
		np = np->prev;
	}
}

void clean(DLLIST *dllistp) {
	NODE *temp, *np = dllistp->start;
	while (np != NULL) {
		temp = np;
		np = np->next;
		free(temp);
	}
	dllistp->start = NULL;
	dllistp->end = NULL;
	dllistp->length = 0;
}
