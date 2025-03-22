from collections import defaultdict

def maxfruits(arr,k):
    n =len(arr)
    l = r= maxlen =0
    mpp = defaultdict(int)
    while r<n:
        mpp[fruits[r]]+=1
        if len(mpp)>k:
            mpp[fruits[l]]-=1
            if mpp[fruits[l]]==0:
                del mpp[fruits[l]]
            l+=1
        if len(mpp)<=k:
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen



fruits = [3,3,3,1,2,1,1,2,3,3,4]
k =2
print(maxfruits(fruits,k))
