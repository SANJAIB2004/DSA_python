def solve(i,j,mat,n,ans,move,vis,di,dj):
    if i==n-1 and j ==n-1:
        ans.append(move)
        return

    dir= "DLRU"
    # dir = "DR"
    for index in range(4):
        nexti = i+di[index]
        nextj = j+dj[index]
        if nexti>=0 and nextj>=0 and nexti<n and nextj<n and vis[nexti][nextj]==0 and mat[nexti][nextj]==1:
            vis[i][j]=1
            solve(nexti,nextj,mat,n,ans,move+dir[index],vis,di,dj)
            vis[i][j]=0

def RatinMaze(mat,n):
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [1,0,0,-1]
    dj = [0,-1,1,0]
    # di = [1,0]
    # dj = [0,1]
    if mat[0][0]==1:
        solve(0,0,mat,n,ans,"",vis,di,dj)
        return ans

if __name__ == "__main__":
    mat = [[1, 0, 0, 0],
           [1, 1, 0, 1],
           [1, 1, 0, 0],
           [0, 1, 1, 1]]
    n = 4
    print(RatinMaze(mat,n)) #['DDRDRR', 'DRDDRR']
