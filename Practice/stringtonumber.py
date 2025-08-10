s = 'onefouroneonezerofour'

words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

res = ''
i = 0
while i<len(s):
    for word,digit in words.items():
        if s.startswith(word,i):
            res+=str(digit)
            i+=len(word)
            break
print(int(res))