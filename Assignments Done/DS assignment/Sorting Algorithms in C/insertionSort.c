//  insertionSort.c
//  Abraar Masud Nafiz
//  ID no: 2019831076

#include <stdio.h>

void printArray(int A[], int n);
void insertionSort(int A[], int n);

int main(void)
{
    int n;
    printf("Enter the number of elements you want to sort : ");
    scanf("%d",&n);
    printf("\nEnter %d elements : ",n);
    int A[n];
    for (int input=0; input<n; input++)
    {
        scanf("%d",&A[input]);
    }
    //int n = sizeof(A) / sizeof(A[0]); //if we want to input A[] manually
    printf("\nPlease wait, Starting insertion sort - \n ");
    printf("At first, the Array is : ");
    printArray(A, n);
    printf("\n");
    
    insertionSort(A, n);
    printf("After sorting, the Array is : ");
    printArray(A, n);
    printf(" \n ");

    return 0;
}


void insertionSort(int A[], int n)
{
    int i,hole;
    for (i=1; i<n; i++)
    {
        int temp = A[i];
        hole = i;
        printf("For %d th iteration, Hole is at index %d and temp is %d \n",i,hole,temp);
        int step=1;
        while (hole>=0 && A[hole-1]>temp)
        {
            printf(" step %d of %d th iteration :-- \n", step,i);
            A[hole] = A[hole-1];
            hole -= 1;
            step += 1;
            printArray(A, n);
            printf("Hole is at index %d  and temp is %d \n",hole,temp);
        }
        step=1;
        A[hole] = temp;
    }
    printf("Sorting is done! \n");
}


void printArray(int A[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf(" %d ", A[i]);
}

/*
 Note for author-
 Time complexity
 best case : sorted array-- O(n) karon while loop ei dhukena
 worst case : reversed array--O(n^2) {while e 1+2+3+4+.....n = n*(n-1)/2 == n^2
 refer to watch?v=i-SKeOcBwko for explaination.
 */
