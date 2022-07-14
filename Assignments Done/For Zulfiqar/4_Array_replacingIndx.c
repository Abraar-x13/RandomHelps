#include<stdio.h>

void replace(int A[], int size, int idx, int num);
void printArray(int A[], int size);

int main(void)
{
    int A[10] = {2, 6, 13, 21, 36, 47, 63 ,81, 97, 104};
    printArray(A, 10);

    replace(A, 10, 3, 99);
    printArray(A, 10);

    return 0;
}

void replace(int A[], int size, int idx, int num)
{
    printf("Replacing %d at index %d with %d\n", A[idx], idx, num);
    A[idx] = num;
}

void printArray(int A[], int size)
{
    for (int i=0; i < size; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}
