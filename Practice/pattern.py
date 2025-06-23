def func(s,n):
    for i in range(1,n+1):
        print('*'*(n-i),end="")
        print(s[:i])




if __name__ == "__main__":
    s = input()
    n = len(s)
    mid = n // 2
    s = s[mid:]+s[:mid]
    print(s)
    func(s,n)
    # func(s)

