# Question 5(a) : Printing Pattern.
def printR(count, num):
    if num == 0:
        return count
    print(count, end=" ")
    return printR(count+1, num-1)

def pattern(n, count, num):
    if n == 0:
        return
    count = printR(1, num)
    print()
    pattern(n - 1, count, num + 1)

if __name__ == '__main__':
    n = int(input("Enter the number of Columns for Pattern from 5(a) : "))
    pattern(n, 1, 1)
