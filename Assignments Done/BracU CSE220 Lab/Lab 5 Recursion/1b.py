# implement a recursive algorithm to find the n-th Fibonacci number.

# from functools import lru_cache
# @lru_cache(maxsize=None)
def Fibonacci(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
# Add the 2 lines above the function if you want to cache the result for optimization.

if __name__ == '__main__':
	nfib = int(input("Enter nth number to find fibonacci: "))
	print(f"The {nfib}th fibonacci number is : {Fibonacci(nfib)}")