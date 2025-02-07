# n =int(input())
# st = [input() for _ in range(n)]
#
# print(st)
# print(" ".join(map(str,st)))

n = int(input())
tim_lis = []

count =0

for tim in tim_lis:
    hour,min = map(int,tim.split(':'))

    if hour > 11 or (hour==11 and min >0 ) :
        count+=1

print(count)


