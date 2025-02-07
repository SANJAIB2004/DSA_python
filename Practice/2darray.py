rows,col = map(int,input().split())
# print(row)
# print(col)

mat = []

for _ in range(rows):
    row = list(map(int,input().split()))
    mat.append(row)


for row in mat:
    #this line is used to print like
    # 1 2 2
    # 1 2 4
    # 1 3 4
    print(" ".join(map(str,row)))