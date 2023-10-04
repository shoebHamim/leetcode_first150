def twoSum(numbers,target):
  n=len(numbers)
  i=0
  checked=None
  while (numbers[i]<=target or numbers[i]<0) and i<n-1:
    j=i+1
    required=target-numbers[i]
    if checked==numbers[i]:
      i+=1
      continue
    while numbers[j-1]<=required and j<n:
      if numbers[j]==required:
        return [i+1,j+1]
      j+=1
    checked=numbers[i]
    i+=1

def twoSum2(numbers,target):
  l,r=0,len(numbers)-1
  while l<r:
    s=numbers[l]+numbers[r]
    if s==target:
      return [l+1,r+1]
    elif s>target:
      r-=1
    else:
      l+=1

      
numbers=[-1,0]
target = -1
print(twoSum2(numbers,target))

