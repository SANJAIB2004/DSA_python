# to get the input for the 2D array, use the following code:

row ,col = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(row)]

for r in matrix:
    print(' '.join(map(str,r)))


# to get the string list input
str1 = list(map(str,input().split()))
for i in str1:
    print(i)
