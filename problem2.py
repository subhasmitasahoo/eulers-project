n = int(input())

prev = 1
cur = 2
sum = 0

while cur <= n:
    if cur%2 == 0:
        sum += cur
    prev, cur = cur, prev+cur

print(sum)
