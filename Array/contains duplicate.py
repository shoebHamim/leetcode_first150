# brute force gives TLE :(
#* this is cpp sets, python ordered set uses hashtable 
''' 
               |     set             | unordered_set
---------------------------------------------------------
Ordering        | increasing  order   | no ordering
                | (by default)        |

Implementation  | Self balancing BST  | Hash Table
                | like Red-Black Tree |  

search time     | log(n)              | O(1) -> Average 
                |                     | O(n) -> Worst Case

Insertion time  | log(n) + Rebalance  | Same as search
                      
Deletion time   | log(n) + Rebalance  | Same as search
'''
# using set/hashing
def containsDuplicate( nums):
  seen_val=set()
  for i in nums:
    if i in seen_val:
      return True
    else:
      seen_val.add(i)
  print(seen_val)

  return False

# sorting
def containsDuplicate2( nums):
  nums.sort()
  for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
      return True
  return False

# interesting one
def containsDuplicate2( nums):
  unique=set()
  for i in nums:
    unique.add(i)
  return len(nums)==len(unique)


print(containsDuplicate([5,4,1,3,2]))


