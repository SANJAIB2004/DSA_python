input = input().strip().split()

stk = []
clip = []

for w in input:
    if w == 'ctrl+c':
        if stk:
            for c in stk:
                clip.append(c)
                print(clip)
        # clip = res.copy()
    elif w == 'ctrl+v':
        if clip:
            for i in clip:
                stk.append(i)
            clip = ''
            print(stk)
        # res.extend(clip)
    else:
        stk.append(w)
print(*stk)


