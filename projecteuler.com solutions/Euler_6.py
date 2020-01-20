# The sum of the squares of the first ten natural numbers is, 385  The square of the sum of the first ten natural
# numbers is 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square
# of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

import math

def findDifference(number):
    sumSquares = 0
    squareSums = 0

    for x in range(1, number + 1):
        sumSquares += math.pow(x, 2)
        squareSums += x
    squareSums = math.pow(squareSums, 2)

    return squareSums - sumSquares


print("The difference is", findDifference(100))
