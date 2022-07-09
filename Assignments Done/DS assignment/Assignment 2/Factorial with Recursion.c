/*Asiignment 10 for Sayma Sultana Chowdhury ma'am
Finding Factorial with Recursion*/
/* Student registration no : 2019831076 */

#include<stdio.h>

long int FACTORL(int n);

int main(void) 
{
    int n;
    printf("Enter Number to find Factorial: ");
    scanf("%d",&n);
    printf("Factorial of %d = %ld", n, FACTORL(n));
    return 0;
}

long int FACTORL(int n) {
    if (n>=1)
        return n*FACTORL(n-1);
    else
        return 1;
}