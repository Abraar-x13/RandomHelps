#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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

if __name__ == '__main__':
    source = [20,10,0,0,0,10,20,30]
    print(palindrome(source,5,5))  # Output: True
    source = [10,20,0,0,0,10,20,30]
    print(palindrome(source,5,5))  # Output: False



