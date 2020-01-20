# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math


def isPalindrome(number):
    number = str(number)
    length = len(number)
    halfway = (math.ceil(length / 2))
    pos1 = 0
    pos2 = length - 1

    while pos1 < halfway <= pos2:
        if number[pos1] != number[pos2]:
            return False
        pos1 += 1
        pos2 -= 1
    return True


largestPalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if isPalindrome(product) and product > largestPalindrome:
            largestPalindrome = product
print("The largest palindrome attainable by calculating the product of two 3-digit numbers is", i, "*", j, "=",
      largestPalindrome)
