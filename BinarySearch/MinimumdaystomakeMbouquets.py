def isPossible(arr, n, k, m, mid):
    count =0
    NoofBouquets =0
    for i in range(n):
        if arr[k] <=mid:
            count+=1
        else:
            NoofBouquets+=count//k
            count =0
    NoofBouquets+=count//k
    return NoofBouquets>=m



def MinDays(arr,k,m):
    n =len(arr)
    low = min(arr)
    high =max(arr)
    while low<=high:
        mid = (low+high)//2
        if isPossible(arr,n,k,m,mid):
            high = mid-1
        else:
            low = mid+1
    return low

arr=[7,7,7,7,13,11,12,7]
k = 3
m=2
print(MinDays(arr,k,m))