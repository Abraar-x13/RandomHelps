//
//  insertionSort.cpp
//  Created by Abraar Masud Nafiz on 6/6/21.
//

#include <iostream>

using namespace std;

void printArray(int A[], int n);
void insertionSort(int A[], int n);


int main()
{
    int n;
    cout<<"Enter the number of elements you want to sort : ";
    cin>>n;
    int A[n];
    
    for (int input=0; input<n; input++)
    {
        cin>>A[input];
    }
    //To check : 12 11 13 5 6
    //int n = sizeof(A) / sizeof(A[0]); //if we input A[] manually
    cout<<"\n Please wait, Starting insertion sort - \n"<<endl;
    cout<<"At first, the Array is : "; printArray(A, n); cout<<endl;
    
    
    insertionSort(A, n);
    
    cout<<endl<<"After sorting, the Array is : "; printArray(A, n); cout<<" \n ";

    return 0;
}


void insertionSort(int A[], int n)
{
    int i,hole;
    for (i=1; i<n; i++)
    {
        int temp = A[i];
        hole = i;
        cout<<"For "<<i<<"th iteration, "<<"Hole is at index "<<hole<<" and temp is "<<temp<<endl;
        int step=1;
        while (hole>=0 && A[hole-1]>temp)
        {
            cout<<" step "<<step<<" of "<<i<<" th iteration :-- ";
            
            cout<<endl;
            A[hole] = A[hole-1];
            hole -= 1;
            step += 1;
            printArray(A, n);
            cout<<"Hole is at index "<<hole<<" and temp is "<<temp<<endl;
            cout<<"\n ";
        }
        step=1;
        A[hole] = temp;
    }
    cout<<"Sorting is done! \n";
}


void printArray(int A[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << A[i] << " ";
}

/*
 
 Time complexity
 best case : sorted array-- O(n) karon while loop ei dhukena
 worst case : reversed array--O(n^2) {while e 1+2+3+4+.....n = n*(n-1)/2 == n^2
 refer to watch?v=i-SKeOcBwko for explaination.
 */
