from collections import deque
def rottingoranges(grid):
    """
Function to determine the time taken for all fresh oranges to rot in a grid.
    :param grid: grid,row,column
    :return: time taken for all fresh oranges to rot, or -1 if impossible

steps:
1. Initialize a queue to keep track of rotten oranges and a counter for fresh oranges.
2. Traverse the grid to find all rotten oranges (value 2) and count fresh oranges (value 1).
3. Use BFS to spread the rot from rotten oranges to adjacent fresh oranges.
4. For each minute, check all rotten oranges and rot adjacent fresh oranges.
5. Increase the time counter for each minute until no fresh oranges remain.
6. Return the time if all fresh oranges rot, otherwise return -1 if any fresh oranges remain.

by sanjai
date: 5/6/2025
    """
    r,c = len(grid), len(grid[0])
    queue = deque()
    time,freshcount = 0,0

    for i in range(r):
        for j in range(c):
            if grid[i][j] ==2:
                queue.append([i,j])
            if grid[i][j] ==1:
                freshcount += 1

    dir = [[-1,0],[1,0],[0,-1],[0,1]]

    while queue and freshcount>0:
        for i in range(len(queue)):
            x,y = queue.popleft()
            for dx,dy in dir:
                nx,ny = x + dx, y + dy
                if nx<0 or nx>=r or ny<0 or ny>=c or grid[nx][ny] != 1:
                    continue

                grid[nx][ny] = 2
                queue.append([nx,ny])
                freshcount -= 1
        time += 1

    return time if freshcount == 0 else -1

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("Time taken to rot all oranges:", rottingoranges(grid))



