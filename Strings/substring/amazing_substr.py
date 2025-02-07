def amazing_substr(str1):
    count =0
    vowel = "aeiouAEIOU"
    for i,char in enumerate(str1):
        if char in vowel:
            count+=len(str1)-i
    return count

str1="abrab"
print(amazing_substr(str1))
# str1 = "i love i menas love"
# lis = str1.split()
# d ={}
# for i in lis:
#     d[i] =d.get(i,0)+1
#     print(d)

