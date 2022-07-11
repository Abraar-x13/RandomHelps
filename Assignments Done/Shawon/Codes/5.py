
def func5(n : int) -> int :
    """
    Computes factorial of a number >= 1.

    Args:
        n (int): num

    Returns:
        int: factorial of that number.
    """    
    if n == 1 : return 1
    else : return n * func5(n - 1)
    

for i in range(1, 10):
    
    print(func5(i))

