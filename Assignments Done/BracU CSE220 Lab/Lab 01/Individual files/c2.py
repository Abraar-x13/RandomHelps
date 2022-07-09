#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"

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


if __name__ == '__main__':
    source_a = [40,50,0,0,0,10,20,30]
    source_b = [10,20,5,0,0,0,0,0,5,40,15,25]
    print(Intersection(source_a, 5, 5, source_b, 8, 7))
    # Output : [10, 20, 40]