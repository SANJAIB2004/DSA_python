def searchinRotatedArrray(arr,k):
    n=len(arr)
    low =0
    high = n-1
    while low<=high:
        mid = low+(high-low)//2

        if arr[mid] == k:
            return mid

        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        #left part is sorted
        if arr[low]<=arr[mid]:
            if arr[low]<=k and k<=arr[mid]:
                high =mid-1
            else:
                low = mid+1
        #right part is sorted
        if arr[mid]<=arr[high]:
            if arr[mid]<=k and k<=arr[high]:
                low = mid+1
            else:
                high =mid-1



arr = list(map(int,input().split()))
k = int(input())
print(searchinRotatedArrray(arr,k))
