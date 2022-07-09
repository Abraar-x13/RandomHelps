# QUESTION 6: Implement binary search algorithm RECURSIVELY
def binary_search(A, low, high, x):
    if high >= low:
        mid = low + (high - low)//2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(A, low, mid - 1, x)
        elif A[mid] < x:
            return binary_search(A, mid + 1, high, x)
    else:
        return -1

if __name__ == '__main__':
    A = [-7, -3, 0, 1, 2, 5, 9, 11]
    element = 9
    idx = binary_search(A, 0, len(A) - 1, element)
    print(f"{element} is present at index {str(idx)}" if idx != -1 else f"{element} is not present in Array")
