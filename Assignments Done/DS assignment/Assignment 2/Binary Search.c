/*Asiignment 5 for Sayma Sultana Chowdhury ma'am
Binary Search*/
/* Student registration no : 2019831076 */

#include <stdio.h> 

// A iterative binary search function. It returns 
// location of x in given array arr[l..r] if present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{ 
    while (l <= r) 
    { 
        int m = l + (r - l) / 2; 
  
        // Check if x is present at mid 
        if (arr[m] == x) { return m; }
  
        // If x greater, ignore left half 
        if (arr[m] < x) { l = m + 1; }
  
        // If x is smaller, ignore right half 
        else r = m - 1; 
    } 
  
    // if we reach here, then element was not present 
    return -1; 
} 
  
int main(void) 
{ 

	int n;
	printf("Size of the array: ");
	scanf("%d", &n);
	printf("Enter the Elemets: \n");
	int arr[n+10];
	for(int i = 0; i < n; i++) 
		scanf("%d", &arr[i]);

	// sorting the array
	for(int i = 0; i < n; i++) 
	{
		for(int j = i + 1; j < n; j++) 
		{
			if(arr[i] > arr[j]) 
			{
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}

	int x;
	printf("Enter the element you want to find in sorted Array : ");
	scanf("%d", &x);

    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", result); 
    return 0; 
} 