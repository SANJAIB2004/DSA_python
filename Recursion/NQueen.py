class Backtrack:
    def NQueen(self,n):
        ans =[]
        leftRow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        board =["."*n for _ in range(n)]
        self.Solve(0,n,board,ans,leftRow,upperDiagonal,lowerDiagonal,n)
        return ans

    def Solve(self, col, n, board, ans, leftRow, upperDiagonal, lowerDiagonal, n1):
        if col == n1:
            ans.append(board[:])
            return

        for row in range(n):
            if leftRow[row]==0 and upperDiagonal[row+col]==0 and lowerDiagonal[n1-1+col-row]==0:

                #place the queens
                board[row] = board[row][:col]+"Q"+board[row][col+1:]
                leftRow[row]=1
                upperDiagonal[row+col]=1
                lowerDiagonal[n1-1+col-row]=1

                self.Solve(col+1,n,board,ans,leftRow,upperDiagonal,lowerDiagonal,n1)

                #to remove the queen
                board[row] = board[row][:col]+"."+board[row][col+1:]
                leftRow[row]=0
                upperDiagonal[row+col]=0
                lowerDiagonal[n1-1+col-row]=0

b = Backtrack()
n = 4
ans = b.NQueen(n) #[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
for i in range(len(ans)):
    print("Arrangement", i+1)
    for j in range(len(ans[0])):
        print(ans[i][j])
        print()


