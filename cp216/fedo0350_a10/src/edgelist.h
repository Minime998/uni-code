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

#ifndef EDGELIST_H
#define EDGELIST_H

// your code document
typedef struct edge {
	int from;
	int to;
	int weight;
	struct edge *next;
} EDGE;

// your code document
typedef struct edgelist {
	int size;
	EDGE *start;
	EDGE *end;
} EDGELIST;

// your code document
EDGELIST* new_edgelist();

// your code document
void add_edge_end(EDGELIST *g, int from, int to, int weight);

// your code document
void add_edge_start(EDGELIST *g, int from, int to, int weight);

// your code document
int weight_edgelist(EDGELIST *g);

// your code document
void display_edgelist(EDGELIST *g);

// your code document
void clean_edgelist(EDGELIST **gp);

#endif
