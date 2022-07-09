# QUESTION 2: Sort an array RECURSIVELY using insertion sort algorithm.

def recurInsertionSort(A, n):
    if n <= 1:
        return
    recurInsertionSort(A, n-1)
    tail, j = A[n-1], n-2
    while (j>=0 and A[j]>tail):
        A[j+1] = A[j]
        j = j-1
    A[j+1] = tail

if __name__ == '__main__':
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    print(f"Original array : {A}")
    recurInsertionSort(A, len(A))
    print(f"After using recursive insertion sort : {A}")
