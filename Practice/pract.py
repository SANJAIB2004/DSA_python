


def fun(s):
    count =0
    for w in s:
        if len(set(w)) >=6:
            count+=1
    return count

s = input()
print(fun(s))