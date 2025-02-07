def countthesubsequencewithsumk(ind,s,n,k,sums):
    if ind == n:
        if sums == k:
            return 1
        return 0
    # pick the element
    sums+=s[ind]
    l = countthesubsequencewithsumk(ind+1,s,n,k,sums)
    # Do not pick the element
    sums-=s[ind]
    r = countthesubsequencewithsumk(ind+1,s,n,k,sums)

    return l+r


s=[1,2,1]
n = len(s)
k = 2
sums = 0
print(countthesubsequencewithsumk(0,s,n,k,sums))