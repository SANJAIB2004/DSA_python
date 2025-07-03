def jumpgame(arr):
    end = 0
    farthest =0
    ans =0
    for i in range(len(arr)-1):
        farthest = max(farthest,i+arr[i])
        if farthest>=len(arr)-1:
            ans+=1
            break
        if i==end:
            ans+=1
            end = farthest
    print(ans)

arr = list(map(int,input().split()))
jumpgame(arr)