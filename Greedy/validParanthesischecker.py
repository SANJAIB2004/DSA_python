def validPar(s):
    lmin,lmax =0,0
    for c in s:
        if c =='(':
            lmin+=1
            lmax+=1
        elif c == ')':
            lmin,lmax = lmin-1,lmax-1
        else:
            lmin,lmax = lmin-1,lmax+1
        if lmin<0:
            lmin =0
        if lmax<0:
            return False
    return lmin==0

s = input()
print(validPar(s))
