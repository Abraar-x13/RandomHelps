//  selectionSort.c
//  Abraar Masud Nafiz
//  ID no: 2019831076

#include <stdio.h>

void PrintArray(int A[], int n);

int main(void)
{
    //Input Array
    int n;
    printf("Enter the number of elements you want to sort : ");
    scanf("%d",&n);
    printf("\nEnter %d elements : ",n);
    int A[n];
    //int n = sizeof(A) / sizeof(A[0]); //if we want to input A[] manually
    for (int input=0; input<n; input++)
    {
        scanf("%d",&A[input]);
    }
    
    printf("At first, the Array is : ");
    PrintArray(A,n);
    printf("\n");
    
    printf("\nPlease wait, Starting insertion sort - \n ");
    
    //Selection Sort
    int step = 1;
    for (int i=0; i<(n-1); i++)
    {
        int indexOfMinArray = i;
        for (int j=i+1; j<n; j++)
        {
            if (A[j]<A[indexOfMinArray]) { indexOfMinArray = j; }
        }
        if (i!=indexOfMinArray)
        {
            printf("Now the array is : \n");
            PrintArray(A,n);
            printf("\n");
            
            printf("In step %d Index of minimum array is %d \n", step,indexOfMinArray);
            int temp = A[i];
            A[i]=A[indexOfMinArray];
            A[indexOfMinArray]= temp;
            
            printf("After swapping, the array is : \n");
            PrintArray(A,n);
            printf("\n");
        }
        else
        {
            printf("In step %d Index of minimum array is the same as step number! (Thus, that index is already sorted ) \n ",step);
            PrintArray(A,n);
            printf("\n");
        }
        step+=1;
        printf("\n");
        printf("\n");
    }
    
    printf("Sorted Array: \n");
    PrintArray(A,n);
    printf("\n");
    
    return 0;
}

void PrintArray(int A[], int n)
{
    for (int i=0; i<n; i++)
    {
        printf(" %d ",A[i]);
    }
}

/*
 Note for author-
 Time complexity O(n^2)

 */
