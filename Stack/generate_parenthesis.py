ans=[]
def backtrack(p,op_count,close_count,n):
  if op_count==close_count==n:
    ans.append(p)
  elif op_count==0 or op_count==close_count:
    backtrack(p+'(',op_count+1,close_count,n)
  if op_count>close_count:
    if op_count<n:
      backtrack(p+'(',op_count+1,close_count,n)
    backtrack(p+')',op_count,close_count+1,n)
backtrack('',0,0,3)
print(ans)