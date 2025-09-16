import re

s = input().strip()

words = re.findall(r'\w+',s)

print(words)

longest_word = max(words,key=len)

print(longest_word)

