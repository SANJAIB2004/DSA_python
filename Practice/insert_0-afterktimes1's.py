def func(lst,k):
    res = []
    count = 0
    for num in lst:
        res.append(num)
        if num == 1:
            count +=1
            if count == k:
                res.append(0)
                count = 0
        else:
            count =0
    return res



if __name__ == "__main__":
    # n,k = map(int,input().split())
    # lst = list(map(int,input().split()))
    n = 5
    k = 1
    lst = [1, 0, 1, 1, 0]

    result = func(lst,k)
    print(*result)
