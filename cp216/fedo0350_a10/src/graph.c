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
#include "queue_stack.h"
#include "graph.h"

GRAPH* new_graph(int order) {

	GRAPH *new = (GRAPH*) malloc(sizeof(GRAPH));
	new->order = order;
	new->size = 0; //initially no edges

	new->nodes = malloc(order * sizeof(GNODE*));
	for (int i = 0; i < order; i++) {
		new->nodes[i] = malloc(sizeof(GNODE)); //create a GNODE object
		new->nodes[i]->nid = i; //set node id to be i
		new->nodes[i]->neighbor = NULL; //initialize neighbor linked list
	}

	return new;
}

void add_edge(GRAPH *g, int from, int to, int weight) {

	GNODE *from_node = g->nodes[from];
	ADJNODE *anp = from_node->neighbor;
	ADJNODE *prev;
	int adjacent = 0;
	int has_neighbors = 0;
	if (anp)
		has_neighbors = 1;
	//check if adjacent
	while (anp && adjacent == 0) {
		if (anp->nid == to) { //neighbor exists
			adjacent = 1;
			anp->weight = weight;
		} else {
			prev = anp;
			anp = anp->next;
		}

	}
	//if nodes are not adjacent then add edge
	if (adjacent == 0) {
		//create a new adjnode
		ADJNODE *new_adj = (ADJNODE*) malloc(sizeof(ADJNODE));
		new_adj->nid = to;
		new_adj->weight = weight;
		new_adj->next = NULL;
		if (has_neighbors == 1) {
			prev->next = new_adj;
		} else {
			from_node->neighbor = new_adj;
		}
		g->size++;
	}
}

void display_bforder(GRAPH *g, int start) {
	if (g == NULL)
		return;
	//get order and set the visited array
	int n = g->order;
	int visited[n];
	int i;
	for (i = 0; i < n; i++) {
		visited[i] = 0;
	}
	//bfs
	QUEUE queue = { 0 };
	GNODE *gnp = NULL;
	ADJNODE *anp = NULL;
	enqueue(&queue, g->nodes[start]);
	visited[start] = 1;
	while (queue.front) {
		gnp = (GNODE*) dequeue(&queue);
		printf("%d ", gnp->nid);
		anp = gnp->neighbor;
		while (anp) {
			i = anp->nid;
			if (visited[i] == 0) {
				enqueue(&queue, g->nodes[i]);
				visited[i] = 1;
			}
			anp = anp->next;
		}
	}
	clean_queue(&queue);
}

void display_dforder(GRAPH *g, int start) {
	int n = g->order;
	int visited[n];
	int i;
	for (i = 0; i < n; i++) {
		visited[i] = 0;
	}

	//dfs
	STACK stack = { 0 };
	GNODE *gnp = NULL;
	ADJNODE *anp = NULL;
	push(&stack, g->nodes[start]);
	visited[start] = 1;

	while ((gnp = peek(&stack))) {
		printf("%d ", gnp->nid);
		pop(&stack);
		anp = gnp->neighbor;
		while (anp) {
			i = anp->nid;
			if (visited[i] == 0) {
				push(&stack, g->nodes[i]);
				visited[i] = 1;
			}
			anp = anp->next;
		}
	}
	clean_stack(&stack);
}

int get_weight(GRAPH *g, int from, int to) {
	ADJNODE *p = g->nodes[from]->neighbor;
	int result = INFINITY;
	while (p) {
		if (p->nid == to) {
			result = p->weight;
			break;
		}
		p = p->next;
	}
	return result;
}

void clean_graph(GRAPH **gp) {
	int i;
	GRAPH *g = *gp;
	ADJNODE *temp, *ptr;
	for (i = 0; i < g->order; i++) {
		ptr = g->nodes[i]->neighbor;
		while (ptr != NULL) {
			temp = ptr;
			ptr = ptr->next;
			free(temp);
		}
		free(g->nodes[i]);
	}
	free(g->nodes);
	free(g);
	*gp = NULL;
}

void display_graph(GRAPH *g) {
	if (g == NULL)
		return;
	printf("order:%d\n", g->order);
	printf("size:%d\n", g->size);
	printf("from:(to weight)");
	int i;
	ADJNODE *ptr;
	for (i = 0; i < g->order; i++) {
		printf("\n%d:", g->nodes[i]->nid);
		ptr = g->nodes[i]->neighbor;
		while (ptr != NULL) {
			printf("(%d %d) ", ptr->nid, ptr->weight);
			ptr = ptr->next;
		}
	}
}
