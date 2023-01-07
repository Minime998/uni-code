/*
 -------------------------------------
 File:    bigint.c
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
#include "bigint.h"
#include "dllist.h"

BIGINT bigint(char *p) {
	BIGINT bigint = { 0 };
	if (p == NULL)
		return bigint;

	else if (!(*p >= '0' && *p <= '9')) {
		return bigint;

	} else if (*p == '0' && *(p + 1) == '\0') {

		insert_end(&bigint, new_node(*p - '0'));
		return bigint;
	} else {
		while (*p) {
			if (*p >= '0' && *p <= '9') {
				insert_end(&bigint, new_node(*p - '0'));
			} else {
				clean(&bigint);
				break;
			}
			p++;
		}
		return bigint;
	}
}

void display_bigint(BIGINT bignumber) {
	NODE *ptr = (NODE*) bignumber.start;

	while (ptr != NULL) {

		printf("%d", ptr->data);
		ptr = (NODE*) ptr->next;
	}
}

BIGINT add(BIGINT op1, BIGINT op2) {
	BIGINT total = bigint(NULL);
	NODE *ptr1 = (NODE*) op1.end;
	NODE *ptr2 = (NODE*) op2.end;
	int c = 0, a, b, s;
	while (ptr1 || ptr2) {
		a = 0;
		b = 0;
		if (ptr1) {
			a = ptr1->data;
			ptr1 = (NODE*) ptr1->prev;
		}
		if (ptr2) {
			b = ptr2->data;
			ptr2 = (NODE*) ptr2->prev;
		}

		s = a + b + c;
		if (s >= 10) {
			insert_start(&total, new_node(s - 10));
			c = 1;
		} else {
			insert_start(&total, new_node(s));
			c = 0;
		}
	}
	if (c == 1) {
		insert_start(&total, new_node(1));
	}
	return total;
}
BIGINT Fibonacci(int n) {
	if (n <= 2) {
		return bigint("1");
	} else {
		BIGINT temp = bigint(NULL);
		BIGINT fib1 = bigint("1");
		BIGINT fib2 = bigint("1");
		int i = 1;
		while (i < n) {
			temp = fib2;
			fib2 = add(fib1, fib2);
			fib1 = temp;
			i++;
		}

		return fib1;
	}
}

