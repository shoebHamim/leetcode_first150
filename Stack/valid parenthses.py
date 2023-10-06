
def isValid( s):
    st=[]
    matching={'(':')','{':'}','[':']'}
    for i in s:
        if i in ['(','{','[']:
            st.append(i)
        else:
            if not st or matching[ st.pop()]!=i:
                return False
           
    return not st

print(isValid('()'))