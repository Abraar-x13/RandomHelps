#include<stdio.h>

int search(int A[], int size, int k);

int main(void)
{
   int A[10] = {2, 6, 13, 21, 36, 47, 63 ,81, 97, 104};
   int khoj = 7;
   int index = search(A, 10, khoj);
   printf("Array te index %d e %d ache.\n",index, khoj);
   return 0;
}

int search(int A[], int size, int k)
{
    for (int i=0; i<size; i++)
    {
        if (A[i] == k)
        {
            printf("for i=%d, A[i]= %d\nCool!!\n",i,k);
            return i;
        }
        printf("for i=%d, A[i]!= %d\n",i,k);
    }
    printf("Eikhane %d nai\n", k);
    return -1;
}
