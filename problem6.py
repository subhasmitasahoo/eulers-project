n = int(input())

sum = (n*(n+1)/2)
sum *= sum

sum -= ((n*(n+1)*(2*n+1))/6)

print(sum)