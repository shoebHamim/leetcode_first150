def largestRectangleArea2(heights):
  heights.sort()
  largest_area=0
  n=len(heights)
  for i in range(n):
    area=heights[i]*(n-i)
    largest_area=max(largest_area,area)
  return largest_area

heights = [2,4]
# only issue with this approach is if the 
# height includes 0
# print(largestRectangleArea2(heights))

def largestRectangleArea(heights):
  max_area=0
  st=[[-1,0]]

  for i,h in enumerate(heights):
    # new elem is bigger/equal, so the prev elem can be extended
    if h>=st[-1][0]:
      st.append([h,i])
    else:
      extened_backto=0
      # extended backto prev_small
      while not st[-1][0]<h:
        popped=st.pop()
        extened_backto=popped[1]
        area=popped[0]*(i-extened_backto)
        max_area=max(area,max_area)
      st.append([h,extened_backto])
  last_limit=len(heights)
  while st[-1][0]!=-1:
    popped=st.pop()
    area=popped[0]*(last_limit-popped[1])
    max_area=max(max_area,area)
  return max_area

heights = [5,5,1,7,1,1,5,2,7,6]
print(largestRectangleArea(heights))


    





