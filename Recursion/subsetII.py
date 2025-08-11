def subsetII(nums):
    temp = []
    ans = []
    n = len(nums)

    def back(i):

        if i==n:
            ans.append(temp[:])
            return

        j = i+1
        while j<n and nums[j] == nums[i]:
            j+=1
        back(j)

        temp.append(nums[i])
        back(i+1)
        temp.pop()

    back(0)
    return ans


nums = list(map(int,input().split()))
print(subsetII(nums))