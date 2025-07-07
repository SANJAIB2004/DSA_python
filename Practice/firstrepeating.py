def firstrepeating(s):
    freq = [0]*26
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        freq[index] +=1

    for i in range(len(s)):
        if freq[ord(s[i])-ord('a')] >1:
            print(f"First repeating character is {s[i]}")
            break


def firstnonrepeating(s):
    freq = [0] * 26
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        freq[index] += 1

    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] ==1:
            print(f"First non repeating character is {s[i]}")
            break


s = input().strip().lower()
firstrepeating(s)
firstnonrepeating(s)