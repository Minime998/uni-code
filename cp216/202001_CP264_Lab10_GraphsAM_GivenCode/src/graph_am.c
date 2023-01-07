/* Grahp representation by adjacent matrix
 * modified from textbook example
 * HBF
 * Version  2019-02-25
 * Version 2020-03-25 Rick Magnotta
 * Version 2022-03-24 Heider Ali
 */

#include "My_Definitions.h"
#include "graph_am.h"

void randomGraph(int adj[][MAX])
//==============================
{
	int i, j, v;

	srand(time(NULL));

	for (i = 0; i < MAX; i++) {
		for (j = 0; j < MAX; j++) {
			if (j == i)
				adj[i][j] = 0;
			else {
				v = rand() % 2;
				adj[i][j] = v;
				adj[j][i] = v;
			}
		}
	}
}

void displayAdjacentMatrix(int adj[][MAX])
//========================================
{
	int i, j;

	printf("    ");
	for (i = 0; i < MAX; i++)
		printf("%d ", i);
	printf("  <=== Node Number\n\n");

	for (i = 0; i < MAX; i++) {
		printf("%d  ", i);

		for (j = 0; j < MAX; j++)
			printf(" %d", adj[i][j]);

		printf("\n");
	}
	printf("^\n");
	printf("|__ Node Number\n");
	printf("\n");
}

void connected(int adj[][MAX],     // Adjacency Matrix
		int node)     // Node in Graph.
//============================
// Given the Graph "adj", and a node "node" present in the graph,
// this routine prints the "node-number" of all the nodes that are
// connected to the node "node".
{
	int index;
	int counter = 0;
	int storevalues[MAX];

	for (index = 0; index <= MAX; index++) {

		if (adj[node][index] == 1 && adj[node][index] == adj[index][node]) {

			storevalues[counter] = index;
			counter++;
		}
	}

	printf("Nodes connected to node %d: [ ", node);

	for (int i = 0; i < counter; i++) {
		if (i + 1 == counter)
			printf("%d ]\n", storevalues[i]);
		else
			printf("%d, ", storevalues[i]);
	}

	return;

}

void node_counts(int adj[][MAX],   // Adjacency Matrix
		int count)   // Target count.
//==============================
// Given the Graph "adj", and the target count "count",
// this routine prints the "node-number" of all the nodes that are
// connected to "count" other nodes.
{
	int timeloops = 0;
	int storevalues[MAX];
	int index = 0;

	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			if (adj[i][j] != 0) {
				timeloops++;
			}
		}
		if (timeloops == count) {
			storevalues[index] = i;
			index++;
		}
		timeloops = 0;
	}

	printf("Nodes connected to %i other nodes: [ ", count);

	if (index == 0)
		printf(" ]\n");

	for (int i = 0; i < index; i++) {
		if (i + 1 != index)
			printf("%d, ", storevalues[i]);
		else
			printf("%d ]\n", storevalues[i]);
	}

	return;
}
