def del_col(c, arr):
    if c < 0 or c >= len(arr[0]):
        return
    for i in range(len(arr)):
        arr[i][c] = '&'

# Matrix input
arr = [
    ['1', '2', '3'],
    ['4', '5', '<'],
    ['6', '7', '8']
]

n = len(arr)
m = len(arr[0])

# Process the matrix
for i in range(n):
    for j in range(m):
        if arr[i][j] == '<':
            del_col(j - 1, arr)
            arr[i][j] = '*'
        elif arr[i][j] == '>':
            del_col(j + 1, arr)
            arr[i][j] = '*'

# Print only '&' characters
for i in range(n):
    for j in range(m):
        if arr[i][j] != '&':
            print(arr[i][j], end=' ')
    print()
