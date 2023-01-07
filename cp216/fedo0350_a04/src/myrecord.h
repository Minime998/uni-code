/*
-------------------------------------
File:    myrecord.h
Project: fedo0350_a04
file description
-------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Version  2022-02-07
-------------------------------------
 */
#ifndef MYRECORD_H
#define MYRECORD_H 

typedef struct {
char name[20];
float score;
} RECORD;

typedef struct {
int count;
float mean;
float stddev;
float median;
} STATS;

char letter_grade(float score);
int import_data(RECORD dataset[], char *filename);  
STATS report_data(RECORD dataset[], int n, char *filename);
 
#endif
