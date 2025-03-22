def assign(cookies,size):
    cookies.sort()
    size.sort()
    n=len(cookies)
    m=len(size)
    l =0
    r=0
    while l<m and r<n:
        if size[l]<=cookies[r]:
            r+=1
        l+=1
    return r

if __name__ == "__main__":
    cookies = list(map(int, input().split()))
    size = list(map(int, input().split()))
    print(assign(cookies, size))

