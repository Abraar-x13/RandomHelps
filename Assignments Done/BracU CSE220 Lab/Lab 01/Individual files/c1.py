#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"

# a method/function that takes in a circular array,
# and start index and finds whether the
# elements in the array form a palindrome or not.
def isPalindromeCircular(a, start_idx, size):
    i = start_idx
    j = start_idx + size - 1
    while i < j:
        # print(f"ai is {a[(i%len(a))]} and aj is {a[(j%len(a))]}")
        if (a[(i%len(a))] != a[(j%len(a))]):
            print("Not Palindrome")
            return
        i += 1
        j -= 1
    print("Palindrome")
    return

if __name__ == '__main__':
    a = [20,10,0,0,0,10,20,30]
    isPalindromeCircular(a, 5, 5)
    a = [10,20,0,0,0,10,20,30]
    isPalindromeCircular(a, 5, 5)



