def containsDuplicate( nums):
  seen_val=set()
  for i in nums:
    if i in seen_val:
      return True
    else:
      seen_val.add(i)
  return False

print(containsDuplicate([1,2,3,4,5]))

