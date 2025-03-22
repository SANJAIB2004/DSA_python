def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i<j:
        while arr[i]<=pivot and i<high:
            i+=1
        while arr[j]>pivot and j>low:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[j],arr[low] = arr[low],arr[j]
    return j



def quicksort(arr,low,high):
    if low<high:
        pivotI = partition(arr,low,high)
        quicksort(arr,low,pivotI-1)
        quicksort(arr,pivotI+1,high)
    
    return arr

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    low ,high = 0,len(arr)-1
    res = quicksort(arr,low,high)
    print(res[:])



