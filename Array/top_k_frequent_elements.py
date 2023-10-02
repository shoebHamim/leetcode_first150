# sorting approach
def topKFrequent(nums,k):
  freq_count={}
  for i in nums:
    current=freq_count.get(i,0)
    freq_count[i]=current+1

  sorted_freq= sorted(freq_count.items(), key=lambda item: item[1],reverse=True)
  ans=[]
  loop=1

  for i in sorted_freq:
    if loop>k:
      break
    loop+=1
    ans.append(i[0])
  return ans
# sorting approach
def topKFrequent2(nums,k):
  freq_count={}
  for i in nums:
    current=freq_count.get(i,0)
    freq_count[i]=current+1
  bucket_sort=[[] for i in range(len(nums))]
  for i,j in freq_count.items():
    bucket_sort[j-1].append(i)
  ans=[]
  found_count=0
  j=len(nums)-1
  while j>-1 and found_count<k:
    if len(bucket_sort[j]):
      ans+=bucket_sort[j]
      found_count+=1
    j-=1
  return ans

nums=[1]
print(topKFrequent2(nums,2))