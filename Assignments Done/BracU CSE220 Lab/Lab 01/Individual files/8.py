#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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

if __name__ == '__main__':
    source = [4,5,6,6,4,3,6,4]
    isThereRepetition(source)  # Output : True
    source = [3,4,6,3,4,7,4,6,8,6,6]
    isThereRepetition(source)  # Output : False
