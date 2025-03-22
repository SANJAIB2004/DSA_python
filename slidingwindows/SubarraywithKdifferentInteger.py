from collections import defaultdict
class Solution:
    def solve(self,nums,k):
        n =len(nums)
        l=r=cnt=0
        mpp =defaultdict(int)
        while r<n:
            mpp[nums[r]]+=1
            while len(mpp)>k:
                mpp[nums[l]]-=1
                if mpp[nums[l]]==0:
                    del mpp[nums[l]]
                l+=1

            if len(mpp)<=k:
                cnt = cnt+(r-l+1)
            r+=1

        return cnt

    def subarraywithkdifferentint(self,nums,k):
        return self.solve(nums,k)-self.solve(nums,k-1)


nums = [1,2,1,2,3]
k=2
sol = Solution()
print(sol.subarraywithkdifferentint(nums,k))