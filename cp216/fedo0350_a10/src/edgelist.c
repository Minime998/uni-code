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
#include "edgelist.h"

EDGELIST* new_edgelist() {

	//create new edgelist structure
	EDGELIST *p = (EDGELIST*) malloc(sizeof(EDGELIST));

	//all the edgelist attributes are set
	p->size = 0;
	p->start = NULL;
	p->end = NULL;

	return p;
}

void add_edge_end(EDGELIST *g, int from, int to, int weight) {

	//to add an edge you need to have an edge in the first place
	EDGE *e = (EDGE*) malloc(sizeof(EDGE));

	//edge attributes set to params
	e->from = from;
	e->to = to;
	e->weight = weight;
	e->next = NULL;

	//if there is an end point already, add edge after the end point
	if (g->end != NULL)
		g->end->next = e;

	//else if the graph is empty, add the edge and it will be the start and finish
	else if (g->start == NULL)
		g->start = e;
	g->end = e;

	g->size++;
}

void add_edge_start(EDGELIST *g, int from, int to, int weight) {

	EDGE *e = (EDGE*) malloc(sizeof(EDGE));

	e->from = from;
	e->to = to;
	e->weight = weight;
	e->next = NULL;

	//if there is a starting edge already, add edge in front of it
	if (g->start != NULL)
		e->next = g->start;

	//else if the graph is empty, add the edge making it both start and finish
	else if (g->end == NULL)
		g->start = e;
	g->end = e;

	g->size++;
}

int weight_edgelist(EDGELIST *g) {

	int sum = 0;
	EDGE *e = (EDGE*) malloc(sizeof(EDGE));

	//start at top of edgelist
	e = g->start;

	while (e) {
		//sum and iterate through
		sum = sum + e->weight;
		e = e->next;
	}

	return sum;
}

void clean_edgelist(EDGELIST **gp) {
	EDGELIST *g = *gp;
	EDGE *temp, *p = g->start;
	while (p) {
		temp = p;
		p = p->next;
		free(temp);
	}
	free(g);
	*gp = NULL;
}

void display_edgelist(EDGELIST *g) {
	if (g == NULL)
		return;
	printf("size:%d\n", g->size);
	printf("(from to weight):");
	EDGE *p = g->start;
	while (p) {
		printf("(%d %d %d) ", p->from, p->to, p->weight);
		p = p->next;
	}
}
