def mergeintervals(intervals):
    n=len(intervals)
    intervals.sort()
    ans =[]
    for i in range(n):
        if not ans or intervals[i][0]>ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1],intervals[i][1])
    return ans

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(mergeintervals(intervals))