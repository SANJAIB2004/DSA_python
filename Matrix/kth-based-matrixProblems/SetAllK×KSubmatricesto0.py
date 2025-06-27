def setallkXkto0(arr,k):
    m,n = len(arr), len(arr[0])
    for i in range(m-k+1):
        for j in range(n-k+1):
            for x in range(k):
                for y in range(k):
                    arr[i+x][j+y] = 0
    return arr

arr = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(setallkXkto0(arr, 2))