def candlebunch(n, k, arr):
    left =0
    right =0

    for i in range(n):
        if arr[i]>k:
            break
        left+=1

    for i in range(n-1,-1,-1):
        if arr[i]>k:
            break
        right+=1
    if left+right>=n:
        return n

    return left+right

# Input handling
n = int(input())  # Number of boxes
k = int(input())  # Max candle requirement
arr = list(map(int, input().split()))  # Array of candle counts

print(candlebunch(n, k, arr))
