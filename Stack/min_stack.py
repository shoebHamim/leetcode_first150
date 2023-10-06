class MinStack:
    def __init__(self):
      self.st=[]
    def push(self,val) :
      self.st.append(val)
    def pop(self) :
      if len(self.st):
          return self.st.pop()
      return 0
    def top(self) :
      if len(self.st):
        return self.st[-1]
      return 0
    def getMin(self):
      minimum=99999999
      backup_stack=MinStack()
      while self.st:
        elem=self.pop()
        minimum=min(elem,minimum)
        backup_stack.push(elem)
      while backup_stack.st:
        a=backup_stack.pop()
        self.push(a)
      return minimum

class MinStack:
    def __init__(self):
      self.st=[]
    def push(self,val) :
        if len(self.st)==0:
            previous_minimum=val
        else:
            previous_minimum=self.getMin()
        self.st.append([val,min(previous_minimum,val)])
    def pop(self) :
        if len(self.st):
            val= self.st.pop()
            return val[0]
        return 0
    def top(self) :
        if len(self.st):
            return self.st[-1][0]
        return 0
    def getMin(self):
        if len(self.st):
            return self.st[-1][1]
        return 0

        
# Your MinStack object will be instantiated and called as such:
minStack =MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin()) 
minStack.pop();
print(minStack.top())    
print(minStack.getMin())