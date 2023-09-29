# sorting and comparing O(nlg(n))
def isAanagram(s,t):
  # s=''.join(sorted(s))
  # t=''.join(sorted(t))
  # return s==t
  return sorted(s)==sorted(t)
# frequency checking of 26 alphabets O(n) mem-> O(n)
def isAanagram2(s,t):
  hash_map={}

  if len(s)!=len(t):
    return False
  arr1=[0]*26
  arr2=[0]*26
  for i in range(len(s)):
    arr1[ord(s[i])-97]+=1
    arr2[ord(t[i])-97]+=1

  for i in range(26):
    if arr1[i]!=arr2[i]:
      return False
  return True

s='anagram'
t='nagarrm'



print(ord('asdf'))
# print(isAanagram2(s,t))



