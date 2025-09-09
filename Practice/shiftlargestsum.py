def shift_lar(i):
    a = list(str(i))
    print(a)
    max_digit = max(a)
    print(max_digit)
    idx = ''.join(a).rfind(max_digit)
    print(idx)

    a[0],a[idx] = a[idx],a[0]
    return int(''.join(a))

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))

    tot = sum(shift_lar(x) for x in l)
    print(tot)





