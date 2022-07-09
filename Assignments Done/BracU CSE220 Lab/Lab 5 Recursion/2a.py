# QUESTION: Implement a recursive algorithm that takes
# a decimal number n and converts n to its corresponding
# (you may return as a string) binary number.

def decToBin(decimal_number):
	if decimal_number == 0:
		return 0
	else:
		v = 10*decToBin(int(decimal_number//2))
		return decimal_number%2 + v

if __name__ == '__main__':
	ndec = int(input("Enter a decimal number: "))
	print(f"The binary of decimal number {ndec} is, {decToBin(ndec)}")
