/*Asiignment 4 for Sayma Sultana Chowdhury ma'am
Bubble Sort : 
Sort an array
Count the number of comparisons Count the number of interchanges */
/* Student registration no : 2019831076 */

#include <stdio.h>

int main()
{
    int n, COMP = 0, INTERCH = 0;
    printf("Size of the array: ");
    scanf("%d", &n);
    int ara[n];
    printf("Enter the elements of the Array: \n");
    for (int i = 0; i < n; ++i) {scanf("%d", &ara[i]);}

    // sorting the array
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n - i; j++)
        {
            COMP++;
            if(ara[j] > ara[j+1]) {
                INTERCH++;
                
                ara[j]   ^= ara[j+1];
                ara[j+1] ^= ara[j];
                ara[j]   ^= ara[j+1];
            }
        }
    }
    //printing the sorted array
    printf("The Sorted Array : \n");
    for (int i = 0; i < n; ++i)
    {
        printf("%d ", ara[i]);
    }
    printf("\n");
    printf("Number of comparisons = %d\n", COMP);
    printf("Number of interchanges = %d\n", INTERCH);

    return 0;
}