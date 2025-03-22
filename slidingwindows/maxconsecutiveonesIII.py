#L.c=>1004

def maxconsecutiveones(nums,k):
    n =len(nums)
    l =r =length = z = maxlen = 0
    while r<n:
        if nums[r] ==0:
            z+=1
        if z>k:
            if nums[l]==0:
                z-=1
            l+=1
        if z<=k:
            length =r-l+1
            maxlen = max(maxlen,length)
        r+=1
    return maxlen


nums = [1,1,1,0,0,0,1,1,1,1,0]
k=2
print(maxconsecutiveones(nums,k))