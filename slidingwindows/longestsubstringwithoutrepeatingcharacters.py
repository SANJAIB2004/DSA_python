#L.c = 3

def longsubstring(str1):
   n =len(str1)
   mpp = [-1]*256
   l=r=0
   length =0
   while r<n:
       if mpp[ord(str1[r])]!=-1:
           l = max(mpp[ord(str1[r])]+1,l)

       mpp[ord(str1[r])] = r

       length = max(length,r-l+1)
       r += 1
   return length


str1 = "abdcabd"
print(longsubstring(str1))
