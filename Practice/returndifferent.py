from collections import Counter
s1 = "the apple is sweet"
s2 = "the apple is sour"

def return_different(s1, s2):
    l1 = s1.split()
    l2 = s2.split()
    res = []

    for word in l1:
        if word not in l2:
            res.append(word)
    for word in l2:
        if word not in l1:
            res.append(word)

    print(*res)
return_different(s1, s2)

