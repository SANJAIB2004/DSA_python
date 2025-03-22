def LongestRepeat(s,k):
    n =len(s)
    l=r=maxlen=maxf=0
    mpp = [0]*26
    while r<n:
        mpp[ord(s[r])-ord('A')]+=1
        maxf = max(maxf,mpp[ord(s[r])-ord('A')])
        length =r-l+1
        if length-maxf >k:
            mpp[ord(s[l])-ord('A')]-=1
            l+=1
        if length-maxf<=k:
            maxlen =max(maxlen,length)
        r+=1
    return maxlen

s = 'ABAB'
k =2
print(LongestRepeat(s,k))