# QUESTION :  Print all the elements of a given Array recursively.

def PrintArray1c(A,i,sz):
    if(i>=sz):
        return
    print(A[i], end=" ")
    PrintArray1c(A, i+1, sz)

if __name__ == '__main__':
    A = []
    sz = int(input("Size of the Array: "))
    print("Enter Elements one one by, pressing enter each time: ")
    for i in range(0, sz):
        num = (int)(input())
        A.append(num)

    print("Array printed recursively: ")
    PrintArray1c(A, 0, sz)
