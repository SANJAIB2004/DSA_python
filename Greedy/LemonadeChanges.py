def lem(changes):
    five=ten=0
    for i in changes:
        if i==5:
            five+=1
        elif i==10:
            if five:
                five-=1
                ten+=1
            else:
                return False
        else:
            if ten and five:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True


if __name__ == '__main__':
    changes = list(map(int, input().split()))
    print(lem(changes))