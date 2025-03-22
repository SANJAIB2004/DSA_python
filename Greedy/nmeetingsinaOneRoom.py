class meeting:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos

class rooms:
    def maxmeeting(self,start,end):
        n=len(start)
        meet = [meeting(start[i],end[i],i) for i in range(n)]
        meet.sort(key=lambda x:x.end)
        count =1
        limit = meet[0].end
        for i in range(1,n):
            if meet[i].start>limit:
                limit = meet[i].end
                count+=1
                break
        return count

if __name__ == "__main__":
    start = [1,3,0,5,8,5]
    end = [2,4,6,7,9,9]
    ob = rooms()
    print(ob.maxmeeting(start,end))
    print("~")