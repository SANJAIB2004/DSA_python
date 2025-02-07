import collections
def groupAnagram(str1):
    freqmpp = collections.defaultdict(list)

    for s in str1:
        key = "".join(sorted(s))
        freqmpp[key].append(s)

    return list(freqmpp.values())

str1 = list(map(str,input().split()))
print(groupAnagram(str1))

