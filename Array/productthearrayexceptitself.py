def productthearrayexceptitself(arr):

    n =len(arr)
    result = [1]*n

    prefix =1
    for i in range(n):
        result[i] = prefix
        prefix*=arr[i]

    suffix =1
    for i in range(len(arr)-1,-1,-1):
        result[i]*=suffix
        suffix*=arr[i]

    return result



arr = list(map(int,input().split()))
result= productthearrayexceptitself(arr)

res = ""
for i in result:
    print(i,end=" ")