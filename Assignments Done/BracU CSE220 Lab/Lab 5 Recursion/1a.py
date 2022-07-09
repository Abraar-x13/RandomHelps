# QUESTION : Implement a recursive algorithm to find factorial of n

# from functools import lru_cache
# @lru_cache(maxsize=None)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
# Add the 2 lines above the function if you want to cache the result for optimization.


if __name__ == '__main__':
    nfact = int(input("Enter a number to find factorial: "))
    print(f"The factorial of {nfact} is {fact(nfact)}")