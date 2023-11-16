# brute force: TLE
def dailyTemp(temperatures):
  n=len(temperatures)
  ans=[]
  for i in range(n):
    count=0
    found=False
    for j in range(i+1,n):
      if temperatures[j]>temperatures[i]:
        count+=1
        ans.append(count)
        found=True
        break
      count+=1
    if not found:
      ans.append(0)
  return ans
print(dailyTemp([30,40,50,60]))

def dailyTemp(temperatures):
  pass