def is_symmetric_kxk(matrix, K):
    n, m = len(matrix), len(matrix[0])
    for i in range(n - K + 1):
        for j in range(m - K + 1):
            symmetric = True
            for x in range(K):
                for y in range(K):
                    if matrix[i + x][j + y] != matrix[i + y][j + x]:
                        symmetric = False
                        break
                if not symmetric:
                    break
                print(f"KxK @({i},{j}) Symmetric? {symmetric}")
matrix = [[1, 2, 3, 4],
            [2, 1, 4, 3],
            [3, 4, 1, 2],
            [4, 3, 2, 1]]
K = 2
is_symmetric_kxk(matrix, K)