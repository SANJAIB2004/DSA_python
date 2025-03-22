#problem l.c = 1432

def maxcards(cards,k):
    n = len(cards)
    if k==n:
        return sum(cards)
    lsum=rsum=maxsum=0
    for i in range(k):
        lsum+=cards[i]
    maxsum =lsum
    rindex = n-1
    for i in range(k-1,-1,-1):
        lsum-=cards[i]
        rsum+=cards[rindex]
        maxsum = max(maxsum,lsum+rsum)
    return maxsum



cards = [1,2,3,4,5,6,1]
k =3
print(maxcards(cards,k))

