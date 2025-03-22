from collections import defaultdict

def maxstr(s,k):
    n =len(s)
    l=r=maxlen=0
    mpp=defaultdict(int)
    while r<n:
        mpp[s[r]]+=1
        if len(mpp)>k:
            mpp[s[l]]-=1
            if mpp[s[l]]==0:
                del mpp[s[l]]
            l+=1
        if len(mpp)<=k:
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen


s ='aaabbccd'
k =2
print(maxstr(s,k))