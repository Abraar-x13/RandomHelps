#include<stdio.h>

void traverse(int A[], int size);

int main(void)
{
   int A[10] = {2, 6, 13, 21, 36, 47, 63 ,81, 97, 104};
   traverse(A, 10);
   return 0;
}

void traverse(int A[], int size)
{
    for (int i=0; i<size; i++)
    {
        printf("%d\n", A[i]);
    }
}
