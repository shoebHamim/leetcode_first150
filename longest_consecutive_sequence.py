
def longestConsecutive(nums):
  s=nums
  s.sort()
  max_count=0
  running_count=0
  running_val=s[0]
  for i in s:
    if i==running_val:
      continue
    if i==running_val+1:
      running_val=i
      running_count+=1
    else:
      max_count=max(running_count,max_count)
      running_val=i
      running_count=0
  max_count=max(running_count,max_count)
  return max_count+1

nums = [1,2,0,1]

# print(longestConsecutive(nums))

# good one
def longestConsecutive2(nums):
  s=set(nums)
  max_count=0
  for i in s:
    if i-1 not in s:
      count=1
      while i+count in s:
        count+=1
      max_count=max(count,max_count)
  return max_count

print(longestConsecutive2([]))

