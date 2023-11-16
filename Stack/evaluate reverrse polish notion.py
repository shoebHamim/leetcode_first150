def evalRPN(tokens):
  st=[]
  for i in tokens:
      if i in '+=*/':
          a=st.pop()
          b=st.pop()
          if i=='+':
              st.append(a+b)
          if i=='-':
              st.append(b-a)
          if i=='*':
              st.append(a*b)
          if i=='/':
              st.append(int(b/a))
      else:
          st.append(int(i))
  return st.pop()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))