# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math

largestPrimeFactor = 0
target = 600851475143

for i in range(2, math.ceil(math.sqrt(target))):
    canDivide = False
    for j in range(2, math.ceil(i / 2) + 1):
        if i % j == 0:
            canDivide = True
            break
    if not canDivide and target % i == 0:
        largestPrimeFactor = i
print("The largest prime factor of 600851475143 is", largestPrimeFactor)

# Alternative (better) solution:
#
# import math
#
# largestPrimeFactor = 0
# target = 600851475143
# smallestPrimeFactor = 0
# for i in range(2, math.ceil(math.sqrt(target))):
#     canDivide = False
#     for j in range(2, math.ceil(i / 2) + 1):
#         if i % j == 0:
#             canDivide = True
#             break
#     if not canDivide and target % i == 0:
#             target = int(target/i)
#             smallestPrimeFactor = i
#     elif target == 1:
#             print("The largest prime factor of 600851475143 is", smallestPrimeFactor)
#             break
