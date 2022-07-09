#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


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


if __name__ == '__main__':
    source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
    removeAll(source, 2)
    print(source)  # Output : [10, 30, 50, 0, 0, 0, 0, 0, 0]


