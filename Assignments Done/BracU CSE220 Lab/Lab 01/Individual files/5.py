#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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

if __name__ == '__main__':
    source = [1, 1, 1, 2, 1] # Output : true
    Splitting_an_Array(source)
    source = [2, 1, 1, 2, 1] # Output : false
    Splitting_an_Array(source)
    source = [10, 3, 1, 2, 10] # Output : true
    Splitting_an_Array(source)
