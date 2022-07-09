#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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
# Justification to not passing the size to this method :
#   In languages like C/C++/Java we actually can't pass an array to a function. We  pass an
#   pointer to the first element, and the size - so the function can use that array. In
#   python, we don't have that problem, so I see no reason to pass size to this function.
#   Please correct me If I'm wrong, as my knowledge is limited compared to yours.


if __name__ == '__main__':
    source  = [10, 20, 30, 40, 50, 0, 0]
    remove(source, 2)
    print(source)
