s = input().strip()
res = []
curr_cnt = 1
curr_ch = s[0]
for i in range(1,len(s)):
    if s[i]==curr_ch:
        curr_cnt += 1

    else:
        res.append(curr_ch)
        res.append(str(curr_cnt))
        curr_cnt =1
        curr_ch = s[i]

res.append(curr_ch)
res.append(str(curr_cnt))

print(''.join(res))
