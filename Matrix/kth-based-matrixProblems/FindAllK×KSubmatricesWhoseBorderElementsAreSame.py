def kxk_border_same(matrix, K):
    n, m = len(matrix), len(matrix[0])
    for i in range(n - K + 1):
        for j in range(m - K + 1):
            val = matrix[i][j]
            all_same = True

            for x in range(K):
                if (matrix[i][j + x] != val or matrix[i + K - 1][j + x] != val or
                    matrix[i + x][j] != val or matrix[i + x][j + K - 1] != val):
                    all_same = False
                    break

            if all_same:
                print(f"\nSame border @({i},{j}) with value {val}:")
                for row in matrix[i:i + K]:
                    print(row[j:j + K])

matrix =   [[1, 2, 1, 1],
            [1, 1, 1, 2],
            [1, 2, 1, 1],
            [2, 1, 1, 1]]
K = 2
kxk_border_same(matrix, K)