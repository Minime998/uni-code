/*
-------------------------------------
File:    polynomial.h
Project: fedo0350_a02
file description
-------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Version  2022-01-24
-------------------------------------
 */

#include<stdio.h>
#include<math.h>
#include<stdbool.h>
#define EPSILON 1e-6

void display_polynomial(float p[], int n, float x)
{
    int c = n;
    for (int i = 0; i < n; i++)
    {
        c-=1;
        if (i+1 == n)
        {
            printf("%0.2f*%0.2f^%i", p[i], x, c);
        }
        else
        {
            printf("%0.2f*%0.2f^%i+", p[i], x, c);
        }
    }
}

float horner(float p[], int n, float x)
{
    float r = 0;
    int i;
    for(i = 0; i < n; i++)
        r = r * x + p[i];
    return r;
}

float bisection(float p[], int n, float a, float b)
{
    
     while (true)
        {
            float c = (a+b)/2;
            if (horner(p, n, c) == 0.0){
                return c;
                break;
            }
            else if (horner(p, n, c)*horner(p, n, a) < 0){
                    b = c;
            }
            else{
                    a = c;
            }
        }
}
