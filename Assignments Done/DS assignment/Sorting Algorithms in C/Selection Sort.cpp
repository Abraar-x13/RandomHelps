//
//  SelectionSort.cpp
//  Created by Abraar Masud Nafiz on 6/6/21.
//

#include <iostream>
using namespace std;

void PrintArray(int A[], int n);

int main(void)
{
    //Input Array
    int n;
    cout<<"Number of elements in Array : ";
    cin>>n;
    int A[n];
    for (int i=0; i<n; i++) { cin>>A[i]; }
    
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
            cout << "Now the array is : \n";
            PrintArray(A,n);
            cout << "\n";
            cout<<"In step "<<step<<", "<<"Index of minimum array is "<<indexOfMinArray;
            cout << "\n";
            int temp = A[i];
            A[i]=A[indexOfMinArray];
            A[indexOfMinArray]= temp;
            cout << "After swapping, the array is : \n";
            PrintArray(A,n);
            cout << "\n";
        }
        else
        {
            cout<<"In step "<<step<<", "<<"Index of minimum array is the same as step number! (Thus, that index is already sorted ) \n ";
            PrintArray(A,n);
            cout << "\n";
        }
        step+=1;
        cout << "\n";
        cout << "\n";
    }
    
    cout << "Sorted Array: \n";
    PrintArray(A,n);
    cout << "\n ";
    
    return 0;
}

void PrintArray(int A[], int n)
{
    for (int i=0; i<n; i++)
    {
        cout << A[i] << " ";
    }
}
