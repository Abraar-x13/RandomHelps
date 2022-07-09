//Assignment 1 for Sayma Sultana Chowdhury ma'am.
/*C Program To Find Maximum And Minimum Element in a dataset using Linear Search */
/* Student registration no : 2019831076 */

#include <stdio.h>
#include <conio.h>
int LS_tofind_MinandMax(int a[],int n);

int main(void)
{
    int a[1000],i,n;
   
    printf("Enter size of the array : ");
    scanf("%d", &n);
 
    printf("Enter elements in array : ");
    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    LS_tofind_MinandMax(a,n);
    return 0;
}

int LS_tofind_MinandMax(int a[],int n)
 {
 	int min,max,i;
 	min=max=a[0];
    for(i=1; i<n; i++)
    {
         if(min>a[i])
		  min=a[i];   
		   if(max<a[i])
		    max=a[i];       
    }
    
    printf("Minimum of the dataset is : %d \n",min);
    printf("Maximum of dataset is : %d",max);
    return 0;
 }