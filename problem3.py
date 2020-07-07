import math

n = int(input())

nRoot = int(math.sqrt(n))

maxPrime = None

while n%2==0:
    maxPrime = 2
    n >>=1

for i in range(3, nRoot+1):
    while n%i == 0:
        maxPrime = i
        n //=i

if n>1:
    maxPrime = n

print(maxPrime)

