/*
 -------------------------------------
 File:    bigint.h
 Project: fedo0350_a03
 file description
 -------------------------------------
 Author:  Noah Fedosoff
 ID:      200420350
 Email:   fedo0350@mylaurier.ca
 Version  2022-01-31
 -------------------------------------
 */
#ifndef BIGINT_H
#define BIGINT_H
#include "dllist.h"

typedef DLLIST BIGINT;
void display_bigint(BIGINT bignumber);
BIGINT bigint(char *digitstr);
BIGINT add(BIGINT oprand1, BIGINT oprand2);
BIGINT Fibonacci(int n);

#endif
