
def printDigits(n : int) -> None:
    """
    Function that displays a triangle with n rows, made of digits.

    Args:
        n (int): number of rows to display.
    """    
    if n == 0 : return
    print(n * str(n))
    printDigits(n-1)


printDigits(5)
printDigits(7)