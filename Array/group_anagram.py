# ascii key approach doesn't work:( because two different string can have same ascii sum

# freq_count key approach
def groupAangrams(strs):
  ans={}
  for s in strs: 
    freq_count=[0]*26
    for i in s:
      freq_count[ord(i)-ord('a')]+=1
    key=tuple(freq_count)
    already=ans.get(key,[])
    already.append(s)
    ans[key]=already

  return ans.values()


# ans=groupAangrams(["eat","tea","tan","ate","nat","bat"])
# print(ans)


# sorted key approach
import collections
def groupAangrams2(strs):
  ans=collections.defaultdict(list)
  for s in strs: 
    key=''.join(sorted(s))
    ans[key].append(s)
 
  return ans.values()

ans=groupAangrams2(["eat","tea","tan","ate","nat","bat"])
print(ans)