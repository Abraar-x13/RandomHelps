# Question 7: Implement a recursive algorithm to
# find the n-th Fibonacci number using memoization.
def fib(num):
    if (num <= 1):
        return num
    F, S = 0, 0
    x=1
    if (A[num-x] != -1):
        F = A[num-x]
    else:
        F = fib(num-x)
    y=2
    if (A[num-y] != -1):
        S = A[num-y]
    else:
        S = fib(num-y)
    return F+S

if __name__ == '__main__':
    A = [-1 for i in range(50)]
    n = 20
    print(fib(n))
