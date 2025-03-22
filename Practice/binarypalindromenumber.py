def binarypalindrome(s):
    count =0
    if bin(s)[2:] == bin(s)[2:][::-1]:
        return 0
    else:
        while s>0:
            s+=1
            count+=1
            if bin(s)[2:] == bin(s)[2:][::-1]:
                return count


n = int(input())
for _ in range(n):
    s = int(input())
    print(binarypalindrome(s))


# sample input
# 3
# 2
# 3
# 4
# sample output
# 1
# 0
# 1


