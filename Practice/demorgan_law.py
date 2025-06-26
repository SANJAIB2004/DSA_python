
# (aub)' = a'n b'
# lhs = s-(a|b)
# rhs = (s-a)&(s-b)
# print(lhs)
# print(rhs)
# print(lhs==rhs)
def first_law(s,a,b):
    first = a.union(b)
    lhs = s.difference(first)


    a_int = s.difference(a)
    b_int = s.difference(b)

    rhs = a_int.intersection(b_int)

    if lhs == rhs:
        print(True)

    else:
        print(False)


def second_law(s,a,b):
    first = a.intersection(b)
    lhs = s.difference(first)

    a_int = s.difference(a)
    b_int = s.difference(b)

    rhs = a_int.union(b_int)

    if lhs == rhs:
        print(True)

    else:
        print(False)

s = {1,2,3,4,5,6,7,8}
a = {1,2,3}
b = {3,4,5}


first_law(s,a,b)
second_law(s,a,b)

#overleaf to check ats












