#include <stdio.h>

void merge(int a[], int m, int b[], int n, int sorted[]) ;

int main(void)
{
    int a[100], m;
    int b[100], n;
    int sorted[200];

    printf("Input number of elements in first array\n");
    scanf("%d", &m);

    printf("Input %d integers\n", m);
    for (int i=0; i<m; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Input number of elements in second array\n");
    scanf("%d", &n);

    printf("Input %d integers\n", n);
    for (int i=0; i<n; i++)
    {
        scanf("%d", &b[i]);
    }

    merge(a, m, b, n, sorted);

    printf("Sorted array:\n");

    for (int i=0; i<m+n; i++)
    {
        printf("%d\n", sorted[i]);
    }

    return 0;
}

void merge(int a[], int m, int b[], int n, int sorted[])
{
    int i, j, k;
    j = k = 0;

    for (i=0; i<m+n;)
    {
        if (j < m && k < n)
        {
            if (a[j] < b[k]) { sorted[i] = a[j]; j++; }
            else  { sorted[i] = b[k]; k++; }
            i++;
        }
        else if (j == m)
        {
            for (; i<m+n;) { sorted[i] = b[k]; k++; i++; }
        }
        else
        {
            for (; i<m+n;) { sorted[i] = a[j]; j++; i++; }
        }
    }
}
