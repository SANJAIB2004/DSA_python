from collections import Counter

num = input().strip()

num = str(int(num))
print(num)

if len(num)==1:
    print(num)

count = {}
for c in num:
    if c not in count:
        count[c]=1
    else:
        count[c]+=1

print(count)

half = []
middle = ''
for d in sorted(count.keys(),reverse=True):
    half.extend(d * (count[d]//2))
    if count[d]%2!=0 and d>middle:
        middle = d
print(half)
palin = (''.join(sorted(half,reverse=True)))+middle+(''.join(sorted(half)))

palin = palin.lstrip('0')
palin = palin.rstrip('0')

print(palin)




