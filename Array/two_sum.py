# brute force
def twoSum(nums,target): #O(n^2)
  for i in range(len(nums)):
    
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return True
  return False

# let's do it in O(n) time ... 
# use hashmap
def twoSum2(nums,target):
  hashmap={}
  for i in range(len(nums)):
    needed=target-nums[i]
    found=hashmap.get(needed)
    if found!=None:
      return [found,i]
    hashmap[nums[i]]=i


nums=[3,2,4]

print(twoSum2(nums,6))
    