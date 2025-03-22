class Comb:
    def combinationSum(self,candidates,target):
        ans=[]
        res=[]
        self.cs(0,target,candidates,res,ans)
        return ans

    def cs(self,index,target,arr,res,ans):
        if index == len(arr):
            if target ==0:
                ans.append(res[:])
            return

        if arr[index]<=target:
            res.append(arr[index])
            self.cs(index,target-arr[index],arr,res,ans)
            res.pop()
        self.cs(index+1,target,arr,res,ans)

c = Comb()
candidates = [2,3,6,7]
target = 7
print(c.combinationSum(candidates,target))