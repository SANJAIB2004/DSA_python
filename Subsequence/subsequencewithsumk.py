def subsequencewithsumk(ind,s,output,n,k,sums):
    if ind == n:
        if sums == k:
            print(output)
        return
    # pick the element
    output.append(s[ind])
    sums += s[ind]
    subsequencewithsumk(ind+1,s,output,n,k,sums)
    # Do not pick the element
    output.pop()
    sums -= s[ind]
    subsequencewithsumk(ind+1,s,output,n,k,sums)

s = [3,1,2]
output = []
n = len(s)
k = 3
sums = 0
subsequencewithsumk(0,s,output,n,k,sums)


