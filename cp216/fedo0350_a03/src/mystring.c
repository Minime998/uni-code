/*
 -------------------------------------
 File:    myatring.c
 Project: fedo0350_a03
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-01-31
 -------------------------------------
 */

#include "mystring.h"
#include <ctype.h>
#define NULL 0

int str_length(char *s) {
	if (s == NULL)
		return -1;
	int counter = 0;
	char *p = s;
	while (*p) {
		counter++;
		p++;
	}
	return counter;
}

int word_count(char *s) {
	if (s == NULL)
		return -1;
	int counter = 0;
	char *p = s;
	int checkflag = 0;
	while (*p) {
		if (*p != ' ' && checkflag == 0) {
			counter++;
			checkflag = 1;
		}

		else if (*p == ' ')
			checkflag = 0;
		p++;
	}
	return counter;
}

void lower_case(char *s) {
	if (s == NULL)
		return;
	char *p = s;
	while (*p) {
		if (*p >= 'A' && *p <= 'Z')
			*p += 32;
		p++;
	};
}

void trim(char *s) {
	char *p = s, *dp = s;
	while (*p < s) {
		if (*p != ' ' || (p > s && *(p - 1) != ' ')) {
			*dp = *p;
			dp++;
		}
		p++;
	}
	s[str_length(s) - 1] = '\0';

}

