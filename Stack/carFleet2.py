
def carFleet(target,position,speed):
  line=sorted(list(zip(position,speed)),reverse=True)
  time=[]
  for i in line:
    time.append((target-i[0])/i[1])
  cur=time[0]
  ans=1
  for t in time:
    if t>cur:
      ans+=1
      cur=t
  return ans

print(carFleet(12, [10,8,0,5,3],[2,4,1,1,3]))