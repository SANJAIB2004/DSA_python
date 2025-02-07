def isPossible(stalls,mid,k):
    cows =1
    last = stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i]-last>=mid:
            cows+=1
            last = stalls[i]
        if cows >= k:
            return True
    return False

def AggressiveCow(stalls,k):
    n = len(stalls)
    stalls.sort()
    low = 1
    high = stalls[n-1] - stalls[0]
    while low<=high:
        mid = (low+high)//2
        if isPossible(stalls,mid,k):
            low =mid+1
        else:
            high = mid-1
    return high

stalls = [0,3,4,7,10,9]
k = 4
print(AggressiveCow(stalls,k))


