
def zerotoones(num):
    # n = str(n)
    # res = ''
    # for i in n:
    #     if i =='0':
    #         res += '1'
    #     else:
    #         res+=i
    # print(res)

    flag = False

    if num < 0:
        flag = True
        num *= -1

    res = 0

    while num > 0:
        rem = num % 10

        if rem == 0:
            res = res*10+1
        else:
            res = res*10 + rem

        num //= 10

    if num == 0 and flag:
        return -res
    else:
        return res

num = int(input())

result = zerotoones(num)

print(result)

print(zerotoones(result))