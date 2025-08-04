def permutationSeq(n,k):
    fact = 1
    nums =[]
    for i in range(1,n):
        fact*=i
        nums.append(i)
    nums.append(n)
    k-=1
    ans = ""
    while True:
        ans+=str(nums[k//fact])
        nums.pop(k//fact)
        if len(nums)==0:
            break
        k%=fact
        fact//=len(nums)
    return ans

n =3
k =6
print(permutationSeq(n,k))