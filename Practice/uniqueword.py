s = input().strip().lower()

# if len(set(s)) == len(s):
#     print(True)
# else:
#     print(False)

freq = [0]*26
for c in s:
    if ord(c)-ord('a') in freq:
        freq[ord(c)-ord('a')] += 1
    else:
        freq[ord(c)-ord('a')] =1
print(freq)
flag =False
for i in freq:
    if i >1:
        flag =True
        break

if flag:
    print(False)
else:
    print(True)
