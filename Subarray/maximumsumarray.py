import sys
def maxsumsubarray(l,n):
    maxi = float('inf')
    maxsum=0
    ansstart,ansend = -1,-1
    for i in range(n):
        if maxsum == 0:
            start = i
        maxsum += l[i]

        if maxsum>maxi:
            maxi = maxsum

            ansstart = start
            ansend = i

        if maxsum <0:
            maxsum=0
    for i in range(ansstart, ansend + 1):
        print(l[i], end=" ")

    return maxsum




l = [-2,4,-5,-9,7,0,2,5]
n= len(l)
print("The maximum sum of the subarray is: ",maxsumsubarray(l,n))
