def anyonesubsequencewithsumk(ind,s,n,k,sums):
    if ind == n:
        if sums == k:
            return True
        return False
    # pick the element
    sums+=s[ind]
    l = anyonesubsequencewithsumk(ind+1,s,n,k,sums)
    # Do not pick the element
    sums-=s[ind]
    r = anyonesubsequencewithsumk(ind+1,s,n,k,sums)

    return l or r

s = [1,2,1]
n = len(s)
k = 2
sums = 0
print(anyonesubsequencewithsumk(0,s,n,k,sums))