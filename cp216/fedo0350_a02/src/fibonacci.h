/*
-------------------------------------
File:    fibonacci.h
Project: fedo0350_a02
file description
-------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
Version  2022-01-24
-------------------------------------
 */

#include <stdio.h>
#include <math.h>

extern int *la;  // global pointer variable to get local variable address

int iterative_fibonacci(int n)
{
  if (&n < la) la = &n;   
  
  int prev = 0;
  int next = 1;
  int fib = prev + next;

  for (int i = 3; i <= n; i++)
  {        
      if (n <= 0)
      {
          return 0;
      }
      
        else if (n <= 2)
      {
          return 1;
      }
      else
      {
        prev = next;
        next = fib;
        fib = prev + next;
      }
   }
  
  return fib;
          
}

int recursive_fibonacci(int n) {

  if (&n < la) la = &n;
  {
      if (n <= 0) return 0;
      if (n <= 2) return 1;
      else return recursive_fibonacci(n-1) + recursive_fibonacci(n-2);
  }
}