def tot(s):
    tem = [-1]*3
    cnt=0
    for i in range(len(s)):
        tem[ord(s[i])-ord('a')]=i
        if tem[0]!=-1 and tem[1]!=-1 and tem[2]!=-1:
            cnt =cnt+(1+min(tem[0],tem[1],tem[2]))
    return cnt

s ='abcabc'
print(tot(s))