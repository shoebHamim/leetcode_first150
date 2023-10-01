
def rotate(nums,k):
  n=len(nums)
  for i in range(n//2):
    nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
  print(nums)
  for i in range((n-k)//2):
    nums[k+i],nums[n-i-1]=nums[n-i-1],nums[k+i]
  for i in range(k//2):
    nums[i],nums[k-1-i]=nums[k-1-i],nums[i]

  print(nums)


nums = [2147483647,-2147483648,33,219,0]
rotate(nums,4)


  
