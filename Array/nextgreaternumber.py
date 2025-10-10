arr = list(map(int,input().split()))
n = len(arr)

res = []

for i in range(n):
    next_greater = 0
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            next_greater = arr[j]
            break
    res.append(next_greater)

print(res)