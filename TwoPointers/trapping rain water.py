# first approach ... little slow :(
def trap1(height):
  # for a element find next bigger element
  # deduct smaller elemnt in between
  # we need two pointer for that
  i=0
  n=len(height)
  ans=0
  while i<n-1:
    if height[i]!=0:
      j=i+1
      if height[j]==height[i]:
        i+=1
      else:
        next_biggest_idx=i+1
        while j<n:
          if height[j]>height[next_biggest_idx]:
            next_biggest_idx=j
          if height[j]>=height[i]:
            width=j-i-1
            ans+=width*height[i]
            start,end=i+1,j
            while start<end:
              ans-=height[start]
              start+=1
            i=j
            break
          elif j==n-1:
            width=next_biggest_idx-i-1
            ans+=width*height[next_biggest_idx]
            start,end=i+1,next_biggest_idx
            while start<end:
              ans-=height[start]
              start+=1
            i=next_biggest_idx
            break
          else:
            j+=1
    else:
      i+=1
  return ans

# now we don't need to deduct in between block by looping

def trap2(height):
  i=0
  n=len(height)
  ans=0
  while i<n-1:
    if height[i]!=0:
      j=i+1
      if height[j]==height[i]:
        i+=1
      else:
        next_biggest_idx=i+1
        in_between=0
        in_between_for_next_biggest=0
        while j<n:
          in_between+=height[j]
          if height[j]>height[next_biggest_idx]:
            next_biggest_idx=j
            in_between_for_next_biggest=in_between-height[j]
          if height[j]>=height[i]:
            width=j-i-1
            ans+=width*height[i]
            ans-=in_between
            ans+=height[j]
            i=j
            break
          elif j==n-1:
            width=next_biggest_idx-i-1
            ans+=width*height[next_biggest_idx]
            ans-=in_between_for_next_biggest
            i=next_biggest_idx
            break
          else:
            j+=1
    else:
      i+=1
  return ans

# print(trap(given))
def trap3(height):
  n=len(height)
  max_left=[0]*n
  max_right=[0]*n
  max_l=height[0]
  for i in range(1,n):
    max_left[i]=max_l
    max_l=max(max_l,height[i])
  max_r=height[n-1]
  for i in range(n-2,-1,-1):
    max_right[i]=max_r
    max_r=max(height[i],max_r)
  ans=0
  for i in range(n):
    temp=min(max_left[i],max_right[i])-height[i]
    if temp>0:
      ans+=temp
  return ans
  

def trap4(height):
  n=len(height)
  ans=0
  i,j=0,n-1
  left_max,right_max=height[i],height[j]
  while i<j:
      if left_max<right_max:
          i+=1
          left_max=max(left_max,height[i])
          ans+=left_max-height[i]
      else:
          j-=1
          right_max=max(right_max,height[j])
          ans+=right_max-height[j]

  return ans
given=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap4(given))
