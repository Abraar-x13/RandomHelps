#include <stdio.h>

int main(void)
{
    int A[2][3]={
                    {1,2,3},
                    {4,5,6}
                };

    int B[2][3]={
                    {7,8,9},
                    {10,11,12}
                };

    int Sum[2][3];

    /* WANT :  */
    /* Sum[0][0] = A[0][0] + B[0][0] */
    /* Sum[0][1] = A[0][1] + B[0][1] */
    /* Sum[0][2] = A[0][2] + B[0][2] */
    /* Sum[1][0] = A[1][0] + B[1][0] */
    /* Sum[1][1] = A[1][1] + B[1][1] */
    /* Sum[1][2] = A[1][2] + B[1][2] */
    /*
    int expectedSum[2][3]={
                              {8, 10, 12},
                              {14, 16, 18}
                          }
    */

    for (int i=0; i<2; i++)
    {
        for (int j=0; j<3; j++)
        {
            Sum[i][j] = A[i][j] + B[i][j];
        }
    }

    for (int i=0; i<2; i++)
    {
        for (int j=0; j<3; j++)
        {
            printf("%d ", Sum[i][j]);
        }
        printf("\n");
    }

    return 0;
}
