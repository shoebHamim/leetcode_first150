def carFleet(target,position,speed):
  time = [(target-p)/s for p,s in sorted(zip(position,speed))]
  print(time)
  ans = cur = 0
  for t in time[::-1]:
      if t > cur:
          ans += 1
          cur = t
  return ans      

      
    



print(carFleet(12, [10,8,0,5,3],[2,4,1,1,3]))
