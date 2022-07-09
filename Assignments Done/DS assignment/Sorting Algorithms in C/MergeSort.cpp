#include <iostream>
using namespace std;

void printArray(int A[], int start, int end);
void merge(int A[], int left_index, int mid, int right_index);
void mergeSort(int A[], int left_index, int right_index);

int STEP = 1;
int main(void)
{
    int n;
    cout<<"Number of elements in Array : ";
    cin>>n;
    int A[n];
    for (int i=0; i<n; i++) { cin>>A[i]; }
    
    cout<<"\nPlease wait, Starting Merge sort - \n"<<endl;
    cout << "At first, the given Array is \n";
    printArray(A, 0, n-1);

    mergeSort(A, 0, n-1);
    
    cout << "\nSorting Finished! \n\nSorted Array is \n";
    printArray(A, 0, n-1);

    return 0;
}

void printArray(int A[], int start, int end)
{
    for(int i=start; i<=end; i++) { cout<<A[i]<<" "; }
    cout << endl;
}


void merge(int A[], int left_index, int mid, int right_index)
{
    STEP++;
    int n1 = mid-left_index + 1;
    int n2 = right_index-mid;

    int Left[n1], Right[n2];

    for (int i=0; i<n1; i++) { Left[i] = A[left_index+i]; }
    for (int j=0; j<n2; j++) { Right[j] = A[mid+1+j]; }

    int i=0, j=0;

    int k=left_index;
    while (i<n1 && j<n2)
    {
        if (Left[i] <= Right[j]) { A[k] = Left[i]; i++; k++; }
        else { A[k] = Right[j]; j++; k++; }
    }
    while(i<n1)
    {
        A[k] = Left[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        A[k] = Right[j];
        j++;
        k++;
    }
    cout<<"Step "<<STEP<<" :- \nMerged: \n";
    printArray(A,left_index,right_index);
    
}



void mergeSort(int A[], int left_index, int right_index)
{
    if(left_index>=right_index){ return; }
    int mid = (right_index+left_index)/2;
    
    STEP++;
    cout<<"Step "<<STEP<<" :- \nDivided into: \n";
    cout<<"Left Array - \n";
    printArray(A,left_index,mid);
    cout<<"AND Right Array - \n";
    printArray(A,mid+1,right_index);
    
    mergeSort(A,left_index,mid);
    mergeSort(A,mid+1,right_index);
    merge(A,left_index,mid,right_index);
}
