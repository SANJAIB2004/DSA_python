def printallsubstring(str1,n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(str1[i:j])
    return




str1 ="SANJAI"
n = len(str1)
printallsubstring(str1,n)
