# QUESTION 1: Sort an array RECURSIVELY using selection sort algorithm.

def recurSelectionSort(A, i, n):
    min = i
    for j in range(i+1, n):
        if A[j] < A[min]:
            min = j
    temp, A[min] = A[min], A[i]
    A[i] = temp
    if i+1 < n:
        recurSelectionSort(A, i+1, n)

if __name__ == '__main__':
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    print(f"Original array : {A}")
    recurSelectionSort(A, 0, len(A))
    print(f"After using recursive selection sort : {A}")