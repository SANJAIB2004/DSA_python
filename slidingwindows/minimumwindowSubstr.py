def minsub(s,t):
    n,m = len(s),len(t)
    l=r=cnt =0
    maxlen = 10**9
    mpp=[0]*256
    sInd =n

    for i in t:
        mpp[ord(i)]+=1

    while r<n:
        if mpp[ord(s[r])]>0:
            cnt+=1
        mpp[ord(s[r])]-=1
        while cnt==m:
            if (r-l+1)<maxlen:
                maxlen =r-l+1
                sInd =1
            mpp[ord(s[l])]+=1
            if mpp[ord(s[l])]>0:
                cnt-=1
            l+=1
        r+=1
    return s[sInd:sInd+maxlen]

s ="ADOBECODEBANC"
t = "ABC"
print(minsub(s,t)) #BANC