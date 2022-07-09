/**Asiignment 3 for Sayma Sultana Chowdhury ma'am
Array Manipulation :
Insert new element so that the array remains sorted
Delete an element so that the array remains sorted*/
/* Student registration no : 2019831076 */

#include <stdio.h>

int main(void)
{
	int n;
	printf("Size of the array: ");
	scanf("%d", &n);
	printf("Enter the Elemets: \n");
	int ara[n+5];
	for(int i = 0; i < n; i++) 
		scanf("%d", &ara[i]);

	// sorting the array
	for(int i = 0; i < n; i++) 
	{
		for(int j = i + 1; j < n; j++) 
		{
			if(ara[i] > ara[j]) 
			{
				int temp = ara[i];
				ara[i] = ara[j];
				ara[j] = temp;
			}
		}
	}

	//Inserting new element
	printf("Enter the element you want to insert: ");
	int x;
	scanf("%d", &x);
	int INDEX = n;
	for(int i = n-1; i >= 0; i--) 
	{
		if(ara[i] <= x) 
		{
			INDEX = i + 1;
			break;
		}
		ara[i+1] = ara[i];
	}
	ara[INDEX] = x;

	// printing the new array
	printf("\nFinal Array: \n");
	for(int i = 0; i < n+1; i++)
		printf("%d ", ara[i]);


	//deleting element from the array
	printf("Enter the element you want to delete: ");
	printf("\n");
	scanf("%d", &x);
	INDEX = -1;
	for(int i = n-1; i >= 0; i--) 
	{
		if(ara[i] == x) { INDEX = i; break; }
	}
	if(INDEX == -1)
		printf("Element Not Found.\n");
	else {
		printf("Succeddfully deleted %d.\n", x);
		for(int i = INDEX; i < n; i++) {
			ara[i] = ara[i+1];
		}
		// printing the new array
		printf("\nYour new array is: \n");
		for(int i = 0; i < n; i++)
			printf("%d ", ara[i]);
		printf("\n");
	}

    return 0;
}
