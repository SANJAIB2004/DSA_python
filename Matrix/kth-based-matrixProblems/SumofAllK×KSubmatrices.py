def sumofallkXksubmat(arr,k):
    n = len(arr)
    m = len(arr[0])

    for i in range(n-k+1):
        for j in range(n-k+1):
            total = 0
            for x in range(k):
                for y in range(k):
                    total += arr[i+x][j+y]
            print(f'Top-left ({i},{j}) sum={total}')


arr =  [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
sumofallkXksubmat(arr, 2)