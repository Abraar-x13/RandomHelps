# TASK - Given pairs of a number and a string, check the parity
# of the number and whether the string is a palindrome or not.

import sys

def check_parity(number):
    global even_parity, odd_parity, no_parity
    f = float(number) - int(float(number))
    if f == 0.0:
        if int(number) % 2 == 0:
            print(f"{number} has even parity", end="")
            even_parity += 1
        else:
            print(f"{number} has odd parity", end="")
            odd_parity += 1
    else:
        print(f"{number} cannot have parity", end="")
        no_parity += 1
    return


def isPalindrome(word):
    global palindromes, not_palindromes
    rev = ''.join(reversed(word))
    if (word == rev):
        print(f"{word} is a palindrome", end="\n")
        palindromes += 1
        return
    else:
        print(f"{word} is not a palindrome", end="\n")
        not_palindromes += 1
    return


if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
    # print(lines)

    global odd_parity, even_parity, no_parity, palindromes, not_palindromes
    odd_parity, even_parity, no_parity = 0, 0, 0
    palindromes, not_palindromes = 0, 0

    original_stdout = sys.stdout
    with open('output.txt', 'w') as f:
        sys.stdout = f
        for line in lines:
            test_case = line.split()
            check_parity(test_case[0])
            print(" and ", end="")
            isPalindrome(test_case[1])
        sys.stdout = original_stdout

    original_stdout = sys.stdout
    with open('record.txt', 'w') as f:
        sys.stdout = f

        odd_parity_perecntage = odd_parity / (even_parity + odd_parity + no_parity) * 100
        print(f"Percentage of odd parity: {odd_parity_perecntage}%")
        even_parity_perecntage = even_parity / (even_parity + odd_parity + no_parity) * 100
        print(f"Percentage of even parity: {even_parity_perecntage}%")
        no_parity_perecntage = no_parity / (even_parity + odd_parity + no_parity) * 100
        print(f"Percentage of no parity: {no_parity_perecntage}%")

        palindrome_perecntage = palindromes / (palindromes + not_palindromes) * 100
        print(f"Percentage of palindrome: {palindrome_perecntage}%")
        not_palindromes_perecntage = not_palindromes / (palindromes + not_palindromes) * 100
        print(f"Percentage of non-palindrome: {not_palindromes_perecntage}%")

        sys.stdout = original_stdout
