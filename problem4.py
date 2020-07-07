def isPalin(n):
    n = str(n)
    return n == n[::-1]


n = int(input()) # no. of digits

a = 10**n - 1
b = a

mini = 10**(n-1)

res = None

while a>=mini:
    b = a
    while b>= mini:
        if isPalin(a*b):
            res = max(res, a*b)
        b -= 1
    a -= 1

print(res)