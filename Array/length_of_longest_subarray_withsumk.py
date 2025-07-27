def subarray(arr,k):
    maxi = 0
    sum = 0
    mpp = {0:-1}

    for i in range(len(arr)):
        sum += arr[i]
        rem = sum-k
        if rem in mpp:
            maxi = max(maxi,i-mpp[rem])
        if sum not in mpp:
            mpp[sum] = i

    return maxi

arr = [-1,1,1]
k = 0
print(subarray(arr,k))
