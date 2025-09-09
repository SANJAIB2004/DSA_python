def sortrowandcol(l,m,n):
    res = []
    for r in l:
        sorting(r)
        res.append(r)
    for r in res:
        print(r)
    for j in range(n):
        cols = [res[i][j] for i in range(m)]
        sorting(cols)
        for i in range(m):
            res[i][j] = cols[i]
    for r in res:
        print(r)

def sorting(l):
    n = len(l)
    for i in range(n):
        for j in range(0,n-1-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

if __name__ == '__main__':
    m,n = map(int,input().split())
    l = [list(map(int,input().split())) for _ in range(m)]
    sortrowandcol(l,m,n)



