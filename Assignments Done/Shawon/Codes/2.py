
def loopCount(num : int) -> int:
    """
        This function returns the sum upto n without using the formula S(n) = n * (n + 1) / 2.

    Args:
        num (int): n of S(n).

    Returns:
        int: Sum upto n.
    """    
    if num == 0 : return num
    else : return num + loopCount(num - 1)

print(loopCount(10))
print(loopCount(100))