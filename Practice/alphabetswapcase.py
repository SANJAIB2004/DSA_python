s = input().strip()

res = ''
i = 0

while i<len(s):
    j = i

    while j<len(s) and s[i].isupper() == s[j].isupper():
        j+=1

    substr = s[i:j]

    if len(substr) >=2:
        res += substr.swapcase()
    else:
        res+=s[i]

    i = j

print(res)

# output:
# breadANDjam
# BREADandJAM