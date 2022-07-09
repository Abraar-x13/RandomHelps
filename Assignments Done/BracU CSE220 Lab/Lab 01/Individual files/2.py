#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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


if __name__ == '__main__':
    source = [10, 20, 30, 40, 50, 60]
    rotateLeft(source, 3)
    # Output : [40, 50, 60, 10, 20, 30]
