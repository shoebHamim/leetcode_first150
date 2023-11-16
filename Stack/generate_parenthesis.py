# ans=[]
# def backtrack2(p,op_count,close_count,n):
#   if op_count==close_count==n:
#     ans.append(p)
#   elif op_count==0 or op_count==close_count:
#     backtrack(p+'(',op_count+1,close_count,n)
#   if op_count>close_count:
#     if op_count<n:
#       backtrack(p+'(',op_count+1,close_count,n)
#     backtrack(p+')',op_count,close_count+1,n)
# backtrack2('',0,0,3)
# print(ans)

# backtrack using stack
ans=[]
st=[]
def backtrack(op_c,cl_c,n):
  if op_c==cl_c==n:
    # empty
    ans.append(''.join(st))
  if cl_c<op_c:
    st.append(')')
    backtrack(op_c,cl_c+1,n)
    st.pop()
  if op_c!=n:
    st.append('(')
    backtrack(op_c+1,cl_c,n)
    st.pop()
backtrack(0,0,3)
print(ans)

