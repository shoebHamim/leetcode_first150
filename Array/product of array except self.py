# using division operation
def productExceptSelf(nums):
  has_0=0
  total_mul=1
  for i in nums:
      if i==0:
          has_0+=1
      else:
          total_mul*=i
  ans=[]
  for i in nums:
    if has_0>1:
      ans.append(0)
    elif has_0==1:
      if i!=0:
        ans.append(0)
      else:
        ans.append(total_mul)
    else:
      ans.append(total_mul//i)
  return ans

# good one :prefix and postfix multiplication technique
def productExceptSelf2(nums):
  n=len(nums)
  pre_mul=[None]*n
  post_mul=[None]*n

  pre_running_mul=1
  post_running_mul=1
  for i in range(n):
    pre_running_mul*=nums[i]
    pre_mul[i]=pre_running_mul

    post_running_mul*=nums[n-i-1]
    post_mul[n-i-1]=post_running_mul
  # simply multiply pre and post mul of each numbers
  print(pre_mul)
  print(post_mul)
  ans=[None]*n
  print(n)
  for i in range(n):
    if i==0:
      ans[i]=post_mul[1]
    elif i==n-1:
      ans[i]=pre_mul[n-2]
    else:
      ans[i]=pre_mul[i-1]*post_mul[i+1]
  return ans
  
# print(productExceptSelf2([-1,1,0,-3,3]))

# concise implementation.. little better too
def productExceptSelf3(nums):
  n=len(nums)
  pre_mul=1
  post_mul=1
  ans=[None]*n
  for i in range(n):
    ans[i]=pre_mul
    pre_mul*=nums[i]
  for i in range(n):
    ans[n-i-1]*=post_mul
    post_mul*=nums[n-i-1]
  return ans

print(productExceptSelf3([-1,1,0,-3,3]))

  