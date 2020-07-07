n = int(input())

arr = [True]*(n+1)

res = 1

for i in range(2, n):
    if arr[i]:
        cur = i
        index = 2
        while(cur*index <= n):
            arr[cur*index] = False
            index += 1

        cur = i
        temp = 1
        while cur*temp <= n:
            temp = cur*temp
            print(temp)
        
        res *= temp

print(res)


