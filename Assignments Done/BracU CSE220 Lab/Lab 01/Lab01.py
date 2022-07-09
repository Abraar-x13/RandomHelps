#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


# Linear Array, Task 1
# Shifts all the elements of the source array to the left by 'k' positions.
def shiftLeft(_source, _k):
    print(f"The Source after being shifted left by {_k} positions:")
    new = []
    if not (_k >= len(_source)):
        # First add the shifted numbers
        for i in range(_k, len(_source)):
            new.append(_source[i])
        # Then add zeros to make 'new' the size of source.
        for i in range(0, _k):
            new.append(0)
        print(new)
    else:
        # This if-else block makes sure that if K is bigger than source,
        # then an array (new) filled with zeros of size of source is printed.
        new = [0] * len(_source)
        print(new)
    return


# Linear Array, Task 2
# This method rotates all the elements of the source array
# to the left by 'k' positions.
def rotateLeft(_source, _k):
    print(f"The Source after rotated left by {_k} positions:")
    new = []
    # Firstly, adding from source[k] to the end
    for x in range(_k, len(_source)):
        new.append(_source[x])
    # Then, adding from source[0] to source[K-1]
    for x in range(0, _k):
        new.append(_source[x])
    print(new)
    return


# Linear Array, Task 3
# This function removes the element in index idx of the source array.
def remove(_source, _idx):
    # Reason for not passing size of source is written at the end of this function.
    new = []
    print(f"Removing {_idx}th index from source.")
    for i in range(0, len(_source)):
        if i!=_idx:
            new.append(_source[i])
    global source
    source = new
    return
# Justification for not passing the size to this method :
#   In languages like C/C++/Java we actually can't pass an array to a function. We  pass an
#   pointer to the first element, and the size - so the function can use that array. In
#   python, we don't have that problem, so I see no reason to pass size to this function.
#   On top of that, the given test cases had passed an array of size 7, yet passed size as 5
#   source=[10,20,30,40,50,0,0] - 7 elements
#   remove(source,size = 5,2) ???
#   Due to this vagueness, I'm not passing the size to the function.
#   Please correct me If I'm wrong, as my knowledge is limited compared to yours.



# Linear Array, Task 4
# This method removes all the occurrences of the given
# element in the source array.
def removeAll(_source, _element):
    print(f"Removing all {_element}'s from source.")
    new = []
    count = 0
    for x in range(0, len(_source)):
        if _source[x] is not _element:
            new.append(_source[x])
        else:
            count += 1
    # In the given example, after the occurences is removed from the source,
    # same number of zeros are appeded at the end. This part imitates that behaviour.
    for p in range(0, count):
        new.append(0)
    global source
    source = new
    return


# Linear Array, Task 5
# 5. Splitting an Array
def Splitting_an_Array(_source):
    right_sum = sum(_source)
    left_sum = 0
    # This loop scans the array from left to right, comparing the sum of left
    # and right sum. If the sums are equal, 'true' is printed, and 'false' if the
    # whole array is scanned but such a balance is not found.
    for x in (_source):
        left_sum += x
        right_sum -= x
        if left_sum == right_sum:
            print("true")
            return
    print("false")
    return


# Linear Array, Task 6
# 6. Array series
def array_series(series):
    new = []
    for n in range (1, series+1):
        if n==series:
            for i in range(0, n):
                new.append(n-i)
                # print(n-i, end=" ")
        else:
            for i in range(0, series-n):
                new.append(0)
                # print(0, end=" ")
            for i in range(0, n):
                new.append(n-i)
                # print(n-i, end=" ")
    return new


# Linear Array, Task 7
#7.Max Bunch Count
def Max_bunch_count(_source):
    max_count, count = 0, 0
    # This loop keeps a counter of how many of the previous numbers were same. And
    # compares it with a variable - max_count. And updates the max_count accordingly.
    for i in range(0, len(_source)-1):
        if _source[i] != _source[i+1]:
            count = 0 # Setting counter to zero when last two numbers were different.
        else:
            count += 1
        if count>max_count:
                max_count = count
    actual_count = max_count + 1
    return actual_count


# Linear Array, Task 8
#  The method returns true if there are at least two
#  elements with the same number of ‘repetition’
def isThereRepetition(_source):
    P = []
    for x in _source:
        n = _source.count(x)
        if (n!=1):
            P.append(n)  # If a number occurs more than once in an array, append it to 'P'
    for x in P:
        n = P.count(x)
        if (n>x):
            print("True")
            # Explaination -
            # If the number of occurrences of occurrence is more then that number,
            # then at least two numbers must have the same number of occurrences.
            return
    print("False")
    return


# Circular Array, Task 1
# A function that takes in a circular array, its size and start index and finds
# whether the elements in the array form a palindrome or not.
def palindrome(_source, start_idx, size):
    index = 0
    length = len(_source)
    i = start_idx
    j = (i+size-1)%length
    flag = None
    while size > index:
        if _source[i] == None or _source[i] == 0:
            i = (i+1)%length
            j = ((j-1)+length)%length
            continue
        if _source[i] != _source[j]:
            flag = False
            return flag
            # If our two pointers i an j point to diffent
            # values in _source, it doesn't form a palindrome.
        else:
            flag = True
        i = (i+1) %length
        j = ((j-1)+length)%length
        index += 1
    return flag


# Circular Array, Task 2
# This function takes two circular arrays, their sizes and start indexes and
# returns a linear array containing the common elements between the two circular arrays.
def Intersection(A, start_idx_a, size_a, B, start_idx_b, size_b,):
    i, count = start_idx_a, 0
    na, nb = [], []
    while count < size_a:
        # print( A[(i%len(A))], end=" " )
        na.append(A[(i%len(A))])
        i += 1
        count += 1
    i, count = start_idx_b, 0
    while count < size_b:
        # print( B[(i%len(B))], end=" " )
        nb.append(B[(i % len(B))])
        i += 1
        count += 1
    # Now, if a value, 'x' esists in Na and Nb then append that to intrsctn
    intrsctn = [x for x in na if x in nb]
    return intrsctn


# Circular Array, Task 3
# Helper function to move players clockwise for
# each generated random number that isn't 1.
def one_turn_clockwise(players):
    new=[]
    for i in range(1, len(players)):
        new.append(players[i])
    new.append(players[0])
    for i in range(0, len(players)):
        players[i] = new[i]
def one_round(players):
    flag_playerNotleft = False
    num = random.randint(0,3)  # a random number between 0 to 3 inclusive.
    if num != 1:
        one_turn_clockwise(players) # Turn once if num is not 1
    else:
        if len(players) == 1:
            print(f"{players[0]} wins!!!")  # Only remaining player must be at 0 idx.
            flag_playerNotleft = True
        else:
            # If more than 1 player is left, player(n/2) gets eliminated.
            rem_idx = int(len(players)/2)
            print(f"Eliminating {players[rem_idx]}")
            players.remove(players[rem_idx])
            print(f"Remaining players are - {players}")
    if flag_playerNotleft:
        return "end"
    else:
        return "not end"


if __name__ == '__main__':
    # Linear Array, Task 1 Test
    source = [10, 20, 30, 40, 50, 60]
    shiftLeft(source, 3)  # Output : [40, 50, 60, 0, 0, 0]

    # Linear Array, Task 2 Test
    source = [10, 20, 30, 40, 50, 60]
    rotateLeft(source, 3)  # Output : [40, 50, 60, 10, 20, 30]

    # Linear Array, Task 3 Test
    source = [10, 20, 30, 40, 50, 0, 0]
    remove(source, 2)
    print(source)  # Output : [ 10,20,40,50,0,0,0]

    # Linear Array, Task 4 Test
    source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
    removeAll(source, 2)
    print(source)  # Output : [10, 30, 50, 0, 0, 0, 0, 0, 0]

    # Linear Array, Task 5 Test
    source = [1, 1, 1, 2, 1] # Output : true
    Splitting_an_Array(source)
    source = [2, 1, 1, 2, 1] # Output : false
    Splitting_an_Array(source)
    source = [10, 3, 1, 2, 10] # Output : true
    Splitting_an_Array(source)

    # Linear Array, Task 6 Test
    print(array_series(4)) # Output : [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]

    # Linear Array, Task 7 Test
    source = [1,2,2,3,4,4,4]
    print(Max_bunch_count(source)) # Output : 3
    source = [1,1,2, 2, 1, 1,1,1]
    print(Max_bunch_count(source)) # Output : 4

    # Linear Array, Task 8 Test
    source = [4,5,6,6,4,3,6,4]
    isThereRepetition(source)  # Output : True
    source = [3,4,6,3,4,7,4,6,8,6,6]
    isThereRepetition(source)  # Output : False

    # Circular Array, Task 1 Test
    source = [20,10,0,0,0,10,20,30]
    print(palindrome(source,5,5))  # Output: True
    source = [10,20,0,0,0,10,20,30]
    print(palindrome(source,5,5))  # Output: False

    # Circular Array, Task 2 Test
    source_a = [40,50,0,0,0,10,20,30]
    source_b = [10,20,5,0,0,0,0,0,5,40,15,25]
    print(Intersection(source_a, 5, 5, source_b, 8, 7))  # Output : [10, 20, 40]

    # Circular Array, Task 3 Test
    players = ["player 1", "player 2", "player 3", "player 4",
              "player 5", "player 6", "player 7"]

    while one_round(players)!= "end":
        one_round(players)
