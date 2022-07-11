
def func7(n : int) -> int :
    """A recursive function that returns the nth element of a geometric sequence.

    Args:
        n (int): nth element of a sequence

    Returns:
        int: value of the nth element.
    """    
    if n == 1 : return 10
    else : return 3 * func7(n -1)
    

print(func7(1))
print(func7(2))
print(func7(3))
print(func7(10))
