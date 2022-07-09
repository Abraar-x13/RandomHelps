# QUESTION 1(a): Implement a recursive algorithm to find factorial of n:
# from functools import lru_cache
# @lru_cache(maxsize=None)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
# Add the 2 lines above the function if you want to cache the result for optimization.


# QUESTION 1(b): Implement a recursive algorithm to find the n-th Fibonacci number:
# from functools import lru_cache
# @lru_cache(maxsize=None)
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
# Add the 2 lines above the function if you want to cache the result for optimization.


# QUESTION 1(c):  Print all the elements of a given Array recursively.
def PrintArray1c(A, i, sz):
    if (i >= sz):
        return
    print(A[i], end=" ")
    PrintArray1c(A, i + 1, sz)


# QUESTION 1(d): Given base and n that are both 1 or more,
# compute recursivelym(no loops) the value of base
# to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(base, power):
    if power == 0:
        return 1
    return base * powerN(base, power - 1)


# QUESTION 2(a): Implement a recursive algorithm that takes
# a decimal number n and converts n to its corresponding
# (you may return as a string) binary number.
def decToBin(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        v2a = 10 * decToBin(int(decimal_number // 2))
        return decimal_number % 2 + v2a


# QUESTION 2(b) : Implement a recursive algorithm
# to add all the elements of a non-dummy headed
# singly linked linear list. Only head of the list
# will be given as parameter where you may assume
# every node can contain only integer as its element.
# Note: you’ll need a Singly Node class for this code.
class Node2b:
    def __init__(self, data):
        self.data = data
        self.next = None


def newNode2b(data):
    new_node = Node2b(data)
    new_node.data = data
    new_node.next = None
    return new_node


# Function to insert a new node at the end of linked list using recursion.
def insertEnd(head, data):
    if (head == None):
        return newNode2b(data)
    else:
        head.next = insertEnd(head.next, data)
    return head


# A Recursive funtion to traverse the LL, finding the sum along the way
def Rtraverse(head):
    global L
    if (head == None):
        return
    L += head.data
    print(head.data, end=" ")
    Rtraverse(head.next)


# QUESTION 2(c): Implement a recursive algorithm which will
# print all the elements of a non-dummy headed singly
# linked linear list in reversed order.
# NOTE from Abraar:
# Write your own class. Or cite GfG

class Node2c:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList2c:
    def __init__(self):
        self.head = None

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr + str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    def push(self, data):
        temp = Node2c(data)
        temp.next = self.head
        self.head = temp


# QUESTION 3 :
# Suppose, you have been given a non-negative integer which is the
# height of a ‘house of cards’. To build such a house you at-least
# require 8 cards. To increase the level (or height) of that house,
# you would require four sides and a base for each level. Therefore,
# for the top level, you would require 8 cards and for each of the
# rest of the levels below you would require 5 extra cards. If you
# were asked to build level one only, you would require just 8 cards.
# Of course, the input can be zero; in that case, you do not build a
# house at all. Complete the recursive method below to calculate the
# number of cards required to build a ‘house of cards’ of specific
# height given by the parameter.
def hocBuilder(height):
    if height == 0:
        return 0
    elif height == 1:
        return 8
    else:
        return 5 + hocBuilder(height - 1)


# Question 5(a) : Printing Pattern.
def printR(count, num):
    if num == 0:
        return count
    print(count, end=" ")
    return printR(count + 1, num - 1)

def pattern(n, count, num):
    if n == 0:
        return
    count = printR(1, num)
    print()
    pattern(n - 1, count, num + 1)


# Question 5(b) : Printing Pattern.
def printL(n, count1=1):
    if count1 == n + 1:
        return 0
    else:
        print(count1, end="")  # Place a space here for pyramid
        printL(n, count1 + 1)

def pattern2(height, count=0, count2=0):
    if height == 0:
        return 0
    else:
        if count2 == 0 and count == 0:
            count2 = height
            count += 1
        if count < height:
            print(" ", end="")
            pattern2(height, count + 1, count2)
        else:
            printL(count2 - count + 1)
            print("")
            pattern2(height - 1, 1, count2)



# QUESTION 6 : Suppose, you are working in a company ‘X’ where your job is to
# calculate the profit based on their investment. If the company invests
# 100,000 USD or less, their profit will be based on 75,000 USD as first
# 25,000 USD goes to set up the business in the first place. For the first
# 100,000 USD, the profit margin is low: 4.5%. Therefore, for every 100
# dollar they spend, they get a profit of 4.5 dollar. For an investment
# greater than 100,000 USD, for the first 100,000 USD (actually on 75,000
# USD as 25,000 is the setup cost), the profit margin is 4.5% where for
# therest,itgoesupto 8%.Forexample,iftheyinvest250,000USD,theywillget an 8%
# profit for the 150,000 USD. In addition, from the rest 100,000 USD, 25,000
# is the setup cost and there will be a 4.5% profit on the rest 75,000.
# Investment will always be greater or equal to 25,000 and multiple of 100.
# Complete the RECURSIVE methods below that take an array of integers
# (investments) and an iterator (always sets to ZERO(‘0’) when the method
# is initially called) and prints the profit for the corresponding
# investment. You must avoid loop and multiplication (‘*’) operator.
class FinalQ:
    def print(self, array: object, idx: object) -> object:
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print("Investment: " + str(array[idx]) + "; Profit: " + str(profit))
            return self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment < 25000:
            return "Investment can't be smaller than 25,000"
        elif investment % 100 != 0:
            return "Investment will always be a multiple of 100"
        elif investment <= 100000:
            return self.case1(investment - 25000)
        else:
            return self.case2(investment - 100000) + self.case1(75000)

    def case1(self, div, count=1):
        if count == 5:
            # v = (div/2)/100
            return div / 200
        else:
            v1 = self.case1(div, count + 1)
            return (div / 100) + v1

    def case2(self, div, count=1):
        if count == 8:
            return div / 100
        else:
            v2 = self.case2(div, count + 1)
            return (div / 100) + v2


# TESTING CODES :


# 1(a) start
nfact = int(input("Enter a number to find factorial: "))
print(f"The factorial of {nfact} is {fact(nfact)}")
# 1(a) end

# 1(b) start
nfib = int(input("Enter nth number to find fibonacci: "))
print(f"The {nfib}th fibonacci number is : {Fibonacci(nfib)}")
# 1(b) end

# 1(c) start
A = []
sz = int(input("Size of the Array: "))
print("Enter Elements one one by, pressing enter each time: ")
for i in range(0, sz):
    num = (int)(input())
    A.append(num)
print("Array printed recursively: ")
PrintArray1c(A, 0, sz)
# 1(c) end

# 1(d) start
nBase = int(input("Enter Base: "))
nPow = int(input("Enter Power: "))
print(f"The result : {powerN(nBase, nPow)} ")
# print(powerN(3, 1)) print(powerN(3, 2)) print(powerN(3, 3))
# 1(d) end

# 2(a) start
ndec = int(input("Enter a decimal number: "))
print(f"The binary of decimal number {ndec} is, {decToBin(ndec)}")
# 2(a) end

# 2(b) start
L = 0  # L is a varible to store the sum
head = None
head = insertEnd(head, 1)
head = insertEnd(head, 2)
head = insertEnd(head, 3)
Rtraverse(head)
print()
print(f"The sum of all the nodes is {L}")
# 2(b) end

# 2(c) start
linkedList = LinkedList2c()
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
print("Original linked list : ")
print(linkedList)
linkedList.head = linkedList.reverse(linkedList.head)
print("Reversed linked list : ")
print(linkedList)
# 2(c) end

# 3 start
h = int(input("Enter a height : "))
print(f"The number of cards required to build a ‘house of cards’ of height {h} is {hocBuilder(h)}")
# 3 end

# 5(a) start
npat1 = int(input("Enter the number of Columns for Pattern from 5(a) : "))
pattern(npat1, 1, 1)
# 5(a) end

# 5(b) start
npat2 = int(input("Enter the number of Columns for Pattern from 5(b) : "))
pattern2(npat2)
# 5(b) end
# 6 start
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)
# 6 end