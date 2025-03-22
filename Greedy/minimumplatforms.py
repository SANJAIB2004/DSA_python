def minimumplatform(arr,dep):
    arr.sort()
    dep.sort()
    n=len(arr)
    i=j=0
    maxlen=0
    count=0
    while i<n:
        if arr[i]<=dep[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        maxlen = max(maxlen,count)
    return maxlen

if __name__ == "__main__":
    arr = [900,940,950,1100,1500,1800]
    dep = [910,1200,1120,1130,1900,2000]
    print(minimumplatform(arr,dep))