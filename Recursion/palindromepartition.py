def ispalindrome(s,start,end):
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def solve(index,s,path,res):
    if index == len(s):
        res.append(path[:])
        return

    for i in range(index,len(s)):
        if ispalindrome(s,index,i):
            path.append(s[index:i+1])
            solve(i+1,s,path,res)
            path.pop()



def palindromepartition(s):
    res=[]
    path=[]
    solve(0,s,path,res)
    return res

s = "aabb"
print(palindromepartition(s)) #[['a', 'a', 'b'], ['aa', 'b']]
