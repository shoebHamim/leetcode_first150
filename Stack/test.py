arr=[4,5,6,6,4,3,6,4]
freq_count=[]

for i in arr:
  count=0
  for j in range(len(arr)):
    if i!=None and i==arr[j]:
      count+=1
      arr[j]=None
  freq_count.append(count)
print(freq_count)







  
