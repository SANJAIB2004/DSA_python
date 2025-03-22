def pap(ds,nums,ans,freq):
    if len(ds) == len(nums):
        ans.append(ds[:])
        return

    for i in range(len(nums)):
        if freq[i]==0:
            freq[i]=1
            ds.append(nums[i])
            pap(ds,nums,ans,freq)
            ds.pop()
            freq[i]=0
def printallPerm(nums):
    ans = []
    ds = []
    freq = [0]*len(nums)
    pap(ds,nums,ans,freq)
    return ans




nums = [1,2,3]
print(printallPerm(nums))