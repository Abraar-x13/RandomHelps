
def matrix_multiplication(A, B, dimension):

    # Initialize C as a nxn zero matrix.
    C = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

    for i in range(0, dimension):
        for j in range(0, dimension):
            for k in range(0, dimension):
                C[i][j] += A[i][k] * B[k][j]

    # Printing the output matrix -
    for i in range(0, dimension):
        print(C[i])

    # Time Complexity : 0(dimension^3).
    # Auxiliary Space: O(dimension^2)


if __name__ == '__main__':

    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 1, 2, 3],
         [4, 5, 6, 7]]

    B = [[9, 8, 7, 6],
         [5, 4, 3, 2],
         [1, 9, 8, 7],
         [6, 5, 4, 3]]

    matrix_multiplication(A, B, 4)


