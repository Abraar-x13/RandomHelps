#include<stdio.h>

void sortKorePrint(int A[], int size);

int main(void)
{
    //input neyar system korte hobe.
   int A[10] = {47, 63, 81, 97, 2, 6, 13, 21, 36, 104};
   sortKorePrint(A, 10);
   return 0;
}

void sortKorePrint(int A[], int size)
{
    for (int i=0; i<size; i++)
    {
        for (int j=i; j<size; j++)
        {
            if (A[j] > A[i])
            {
                int temp = A[j];
                A[j] = A[i];
                A[i] = temp;
            }
        }
    }

    for (int i=0; i<size; i++)
    {
        printf("%d\n", A[i]);
    }
}
