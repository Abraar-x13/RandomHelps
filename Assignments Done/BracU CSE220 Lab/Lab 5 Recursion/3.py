# QUESTION :
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
    if height==0:
        return 0
    elif height==1:
        return 8
    else: return 5+hocBuilder(height-1)

if __name__ == '__main__':
    h = int(input("Enter a height : "))
    print(f"The number of cards required to build a ‘house of cards’ of height {h} is {hocBuilder(h)}")
