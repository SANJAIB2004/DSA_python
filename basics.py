# # to get the input for the 2D array, use the following code:
#
# row ,col = map(int,input().split())
#
# matrix = [list(map(int,input().split())) for _ in range(row)]
#
# for r in matrix:
#     print(' '.join(map(str,r)))
#
#
# # to get the string list input
# str1 = list(map(str,input().split()))
# for i in str1:
#     print(i)

n = 8

print(bin(n)[2:])
print(n&1)
def reverse_bit(n):
    r = 0
    for i in range(n):
        r = (r<<1)|(n&1)
        n>>=1
    print(bin(r)[2:])
reverse_bit(n)

kth border pattern:

7 2

* * * * * * *
* # # # # # *
* # * * * # *
* # * * * # *
* # * * * # *
* # * * * # *
* # # # # # *


