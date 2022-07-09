#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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


if __name__ == '__main__':
    source = [1,2,2,3,4,4,4]
    print(Max_bunch_count(source)) # Output : 3
    source = [1,1,2, 2, 1, 1,1,1]
    print(Max_bunch_count(source)) # Output : 4

