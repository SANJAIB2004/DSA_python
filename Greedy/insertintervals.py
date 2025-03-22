def insertintervals(intervals,newinterval):
    res = []
    n=len(intervals)
    i=0

    #left side
    while i<n and intervals[i][1]<newinterval[0]:
        res.append(intervals[i])
        i+=1

    while i<n and intervals[i][0]<=newinterval[1]:
        newinterval[0] = min(newinterval[0],intervals[i][0])
        newinterval[1] = max(newinterval[1],intervals[i][1])
        i+=1
    res.append(newinterval)

    #remaining
    while i<n:
        res.append(intervals[i])
        i+=1

    return res

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newinterval = [2,5]
    print(insertintervals(intervals,newinterval))



