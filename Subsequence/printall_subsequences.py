def printsubsequences(ind,s,output,n):
    if ind== n:
        print(output)
        return
    # pick the element
    # if we use this order we can get the null as first element
    printsubsequences(ind + 1, s, output, n)
    output.append(s[ind])
    printsubsequences(ind+1,s,output,n)
    # Do not pick the element
    output.pop()
    # if we use this order we can get the null as last element
    # printsubsequences(ind+1,s,output,n)

s = [3,1,2]
output = []
n = len(s)
printsubsequences(0,s,output,n)

