/*
 -------------------------
 File: File Name
 Project: Project name
 -------------------------
 Author: Noah Fedosoff
 ID: 200420350
 Email: fedo0350@mylaurier.ca
 Version YYYY-MM-DD
 -------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hash.h"

extern int htsize;

extern int htsize;

int hash(char *word) {
	unsigned int hash = 0, i;
	for (i = 0; word[i] != '\0'; i++) {
		hash = 31 * hash + word[i];
	}
	return hash % htsize;
}

HSNODE* new_hashnode(char *key, int value) {

	HSNODE *node = (HSNODE*) malloc(sizeof(HSNODE));

	strcpy(node->key, key);
	node->value = value;
	node->next = NULL;

	return node;
}

HASHTABLE* new_hashtable(int size) {

	HASHTABLE *table = (HASHTABLE*) malloc(sizeof(HASHTABLE));
	table->hna = (HSNODE**) malloc(sizeof(HSNODE**) * size);

	for (int i = 0; i <= size; i++)
		*(table->hna + i) = NULL;

	table->size = size;
	table->count = 0;

	return table;
}

HSNODE* search(HASHTABLE *ht, char *key) {

	int i = hash(key);

	HSNODE *j = *(ht->hna + i);

	if (j != NULL)
		while (j != NULL) {
			if (strcmp(j->key, key) == 0) {
				return j;
			}
			j = j->next;

		}

	return NULL;

}

int insert(HASHTABLE *ht, HSNODE *np) {

	int key = hash(np->key);

	HSNODE *n = ht->hna[key];

	if (n == NULL) {
		if (ht->count == ht->size)
			return 0;
		else {
			ht->hna[key] = np;
			ht->count++;

			return 1;
		}
	} else {
		if (strcmp(n->key, np->key) == 0) {
			ht->hna[key]->value += np->value;

			return 0;
		} else {
			HSNODE *nn = ht->hna[key];

			while (nn->next != NULL) {
				nn = nn->next;
			}

			nn->next = np;

			ht->count++;
			return 1;
		}
	}
	return 0;
}

int delete(HASHTABLE *ht, char *key) {

	int i = hash(key);
	HSNODE *p = ht->hna[i], *pp = NULL;

	if (p != NULL) {
		while (p && strcmp(key, p->key) > 0) {
			pp = p;
			p = p->next;
		}

		if (p && strcmp(key, p->key) == 0) {

			if (pp)
				pp->next = p->next;
			else
				*(ht->hna + i) = NULL;

			ht->count--;
			return 1;

		}
	}
	return 0;
}

void clean_hash(HASHTABLE **htp) {
	if (*htp == NULL)
		return;
	HASHTABLE *ht = *htp;
	HSNODE *sp = ht->hna[0], *p, *temp;
	int i;
	for (i = 0; i < ht->size; i++) {
		p = ht->hna[i];
		while (p) {
			temp = p;
			p = p->next;
			free(temp);
		}
		ht->hna[i] = NULL;
	}
	free(ht->hna);
	ht->hna = NULL;
	*htp = NULL;
}
