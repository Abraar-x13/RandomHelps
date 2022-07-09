#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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


if __name__ == '__main__':
    source = [10, 20, 30, 40, 50, 60]
    shiftLeft(source, 3)
    # Output : [40, 50, 60, 0, 0, 0]

