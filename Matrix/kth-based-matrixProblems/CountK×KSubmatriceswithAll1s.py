def countkXksubmat(arr,k):
    m,n = len(arr), len(arr[0])
    count =0
    for i in range(m-k+1):
        for j in range(n-k+1):
            all_ones = True
            for x in range(k):
                for y in range(k):
                    if arr[i+x][j+y]!=1:
                        all_ones = False
                        break
                if not all_ones:
                    break
            if all_ones:
                count += 1
    print(f'Number of {k}x{k} submatrices with all 1s: {count}')



arr = [[1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]]
countkXksubmat(arr, 2)