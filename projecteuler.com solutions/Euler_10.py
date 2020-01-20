import math

primeNumbers = [2]
primeSum = 2

for i in range(3, 2000001, 2):
    divisors = 0
    isPrime = True
    for j in range(0, math.ceil(len(primeNumbers)/2)):
        if i % primeNumbers[j] == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(i)
        primeSum += i

print(primeSum)
