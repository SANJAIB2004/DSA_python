class CSII:
    def comsum(self, candidates, target):
        res = []
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0,ans, res)
        return res

    def dfs(self, candidates, target, index, ans, res):
        if target == 0:
            res.append(ans[:])
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            ans.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i+1, ans, res)
            ans.pop()

c = CSII()
candidates = [10,1,2,7,6,1,5]
target = 8
print(c.comsum(candidates,target)) #[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]