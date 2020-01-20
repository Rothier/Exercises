# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

notFound = True

while notFound:
    for i in range(1, 999):
        iSquared = i**2
        for j in range(1, 998):
            jSquared = j**2
            kSquared = i**2 + j**2
            k = math.sqrt(kSquared)
            if i+j+k == 1000:
                print(i, "squared and", j, "squared equals", int(k), "squared")
                print(i, "+", j, "+", int(k), "=", int(i+j+k))
                print("Product =", i, "*", j, "*", int(k), "=", int(i*j*k))
                notFound = False
        if not notFound:
            break
