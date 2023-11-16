
def dailyTemperatures2(temperatures):
  i=0
  n=len(temperatures)
  ans=[0]*n
  while i<n:
    selected=temperatures[i]
    wait=1
    for j in range(i+1,n):
      if temperatures[j]>selected:
          ans[i]=wait
          break
      wait+=1
    i+=1
  return ans


def dailyTemperatures(temperatures):
  temp_st=[]
  temp_st.append([temperatures[0],0])
  ans=[0]*len(temperatures)
  for i,temp in enumerate(temperatures):
    while temp>temp_st[-1][0]:
      elem=temp_st.pop()
      ans[elem[1]]=i-elem[1]
      if not temp_st:
        break
    temp_st.append([temp,i])
  return ans
              
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
        