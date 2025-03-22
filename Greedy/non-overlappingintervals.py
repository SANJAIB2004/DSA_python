def nonoverlapping(intervals):
    n=len(intervals)
    intervals.sort(key = lambda x:x[1])
    count =1
    limit = intervals[0][1]

    for i in range(1,n):
        if intervals[i][0]>=limit:
            limit = intervals[i][1]
            count+=1

    return n-count

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(nonoverlapping(intervals))