
def func6(n : int) -> int :
    """A recursive function that returns the nth element of a arithmetic sequence.
 
    Args:
        n (int): nth element of a sequence

    Returns:
        int: value of the nth element.
    """    
    if n == 1 : return 10
    else : return 20 + func6(n -1)
    

print(func6(1))
print(func6(2))
print(func6(3))
print(func6(10))
