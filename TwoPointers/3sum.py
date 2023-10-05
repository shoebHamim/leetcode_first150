def twoSum(nums,target,skip,val):
  hashmap={}
  ans=[]
  for i in range(len(nums)):
    if i==skip:
      continue
    needed=target-nums[i]
    found=hashmap.get(needed)
    if found!=None:
      cur_ans=[nums[found],nums[i],val]
      cur_ans.sort()
      ans.append(cur_ans)
    hashmap[nums[i]]=i
  return ans

def threeSum(nums):
  checked=None
  ans=[]
  n=len(nums)
  for i in range(n):
    if checked==nums[i]:
      continue
    target=-nums[i]
    available=twoSum(nums,target,i,nums[i])
    if available:
      for a in available:
        if a not in ans:
          ans.append(a)
    checked=nums[i]
  return ans

def twoSum2(numbers,l,target):
  ans=[]
  r=len(numbers)-1
  while l<r:
    s=numbers[l]+numbers[r]
    if s==target:
      ans.append([-target,numbers[l],numbers[r]])
      l+=1
      r-=1
      while numbers[l]==numbers[l-1] and l<=r:
        l+=1

    elif s>target:
      r-=1
    else:
      l+=1
  return ans

def threeSum2(nums):
  nums.sort()
  n=len(nums)
  l=0
  ans=[]
  while l<n:
    if l>0 and nums[l-1]==nums[l]:
      l+=1
      continue
    available=twoSum2(nums,l+1,-nums[l])
    if available:
      ans+=available
    l+=1
  return ans

nums =[-2,0,0,2,2]

print(threeSum2(nums))