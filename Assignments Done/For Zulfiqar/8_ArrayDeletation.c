#include <stdio.h>

int main(void)
{
   int position;
   int A[10] = {2, 6, 13, 21, 36, 47, 63 ,81, 97, 104};
   int n = 10;

   printf("Enter the th number you want to delete\n");
   scanf("%d", &position);

   if (position >= n+1)
   {
       printf("Deletion not possible.\n");
   }
   else
   {
      for (int c = position-1; c <n-1; c++)
      {
          A[c] = A[c+1];
      }

      printf("Resultant array:\n");

      for (int i=0; i<n-1; i++)
      {
          printf("%d\n", A[i]);
      }
   }

   return 0;
}
