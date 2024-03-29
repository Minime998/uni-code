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
#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expression_symbol.h"

int get_priority(char op) {
	if (op == '/' || op == '*' || op == '%')
		return 1;
	else if (op == '+' || op == '-')
		return 0;
	else
		return -1;
}

int type(char c) {
	if (c >= '0' && c <= '9')
		return 0;
	else if (c == '/' || c == '*' || c == '%' || c == '+' || c == '-')
		return 1;
	else if (c == '(')
		return 2;
	else if (c == ')')
		return 3;
	else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		return 5;
	else
		return 4;
}

QUEUE infix_to_postfix_symbol(char *infixstr, HASHTABLE *ht) {
	QUEUE queue = { 0 };
	STACK stack = { 0 };
	char *p = infixstr;
	int num = 0;
	NODE *temp = { 0 };

	while (*p) {
		char symbol[11] = { 0 };

		if (*p >= '0' && *p <= '9') {

			num = *p - '0';
			while ((*(p + 1) >= '0' && *(p + 1) <= '9')) {
				num = num * 10 + *(p + 1) - '0';
				p++;
			}
			enqueue(&queue, new_node(num, 0));
		}

		else if (*p == '(') {
			push(&stack, new_node(*p, type(*p)));
		}

		else if (*p == ')') {
			while (stack.top && (temp = pop(&stack))->type != 2) {
				enqueue(&queue, temp);
			}
		}

		else if (type(*p) == 1) {

			while (stack.top
					&& get_priority(*p) <= get_priority(stack.top->data)) {
				enqueue(&queue, pop(&stack));
			}
			push(&stack, new_node(*p, type(*p)));

		} else if (type(*p) == 5) {

			strncat(symbol, p, 1);

			while ((*(p + 1) >= 'a' && *(p + 1) <= 'z')
					|| (*(p + 1) >= 'A' && *(p + 1) <= 'Z')) {
				strncat(symbol, (p + 1), 1);

				p++;
			}

			HSNODE *result = search(ht, symbol);
			enqueue(&queue, new_node(result->value, 0));
		}
		p++;
	}

	while (stack.top) {
		enqueue(&queue, pop(&stack));
	}
	return queue;
}

int evaluate_infix_symbol(char *infixstr, HASHTABLE *ht) {
	QUEUE queue = infix_to_postfix_symbol(infixstr, ht);
	int result = evaluate_postfix(queue);
	return result;
}

int evaluate_postfix(QUEUE queue) {

	STACK stack = { 0 };
	NODE *p = queue.front;
	int type = 0;
	int result = 0;
	while (p) {

		type = p->type;
		if (type == 0) {

			push(&stack, new_node(p->data, 0));

		} else if (type == 1) {

			NODE *b = pop(&stack);
			NODE *a = pop(&stack);
			NODE *c = new_node(0, 0);

			switch (p->data) {

			case '+':

				c->data = a->data + b->data;
				break;
			case '-':

				c->data = a->data - b->data;
				break;
			case '*':

				c->data = a->data * b->data;
				break;
			case '/':

				c->data = a->data / b->data;
				break;
			}

			push(&stack, c);
		}
		p = p->next;
	}

	if (stack.top != NULL) {

		result = stack.top->data;
	}
	return result;
}

