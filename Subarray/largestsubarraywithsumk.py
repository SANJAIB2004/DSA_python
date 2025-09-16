def largestsubarraywithsumk(arr,k):
    sum =0
    maxlen=0
    prefixsum ={}
    for i in range(len(arr)):
        sum+=arr[i]
        if sum ==k:
            maxlen = max(maxlen,i+1)

        rem = sum-k
        if rem in prefixsum:
            length = i - prefixsum[rem]
            maxlen = max(maxlen,length)

        if sum not in prefixsum:
            prefixsum[sum] = i
    return maxlen




arr = list(map(int,input().strip().split()))
k = int(input())
print(largestsubarraywithsumk(arr,k))
