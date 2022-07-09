#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"

# 6. Array series
def array_series(series):
    new = []
    for n in range (1, series+1):
        if n==series:
            for i in range(0, n):
                new.append(n-i)
                # print(n-i, end=" ")
        else:
            for i in range(0, series-n):
                new.append(0)
                # print(0, end=" ")
            for i in range(0, n):
                new.append(n-i)
                # print(n-i, end=" ")
    return new


if __name__ == '__main__':
    print(array_series(4))
    # Output : [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
