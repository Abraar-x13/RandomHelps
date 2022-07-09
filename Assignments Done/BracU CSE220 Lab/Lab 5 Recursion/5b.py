# Printing Pattern :
def printL(n, count1=1):
    if count1 == n + 1:
        return 0
    else:
        print(count1, end="") # Place a space here for pyramid
        printL(n, count1 + 1)

def pattern2(height, count=0, count2=0):
    if height == 0:
        return 0
    else:
        if count2 == 0 and count == 0:
            count2 = height
            count += 1
        if count < height:
            print(" ", end="")
            pattern2(height, count + 1, count2)
        else:
            printL(count2 - count + 1)
            print("")
            pattern2(height - 1, 1, count2)


if __name__ == '__main__':
    n = int(input("Enter the number of Columns for Pattern from 5(b) : "))
    pattern2(n)
