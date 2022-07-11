def myParityCount(n : int) -> str:
    """
        This function returns the parity of a binary string passed to it.

    Args:
        n (int): binary string

    Returns:
        str: odd or even.
    """    
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return "Odd" if parity == -1 else "Even"


nums = ["01001010", "11011011", "00110101", "00101010"]
for num in nums :
    n = int(num, 2)
    print(f"Parity of {num} is : {myParityCount(n)}")
