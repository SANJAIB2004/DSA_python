def merge(arr,low,mid,high):
    result =[]
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            result.append(arr[left])
            left+=1
        else:
            result.append(arr[right])
            right+=1
    while left<=mid:
        result.append(arr[left])
        left+=1
    while right<=high:
        result.append(arr[right])
        right+=1

    for i in range(len(result)):
        arr[low+i] = result[i]

def mergesort(arr,low,high):
    if low==high:
        return
    mid = (low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)



arr = [1,4,5,3,8]
mergesort(arr,0,len(arr)-1)
print(arr)

