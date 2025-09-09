a,b = map(int,input().split())
l = list(map(int,input().split()))

for i in range(a-b+1):
    window = l[i:i+b]
    arr = sorted(window)[:2]
    print(arr[0],arr[1])



