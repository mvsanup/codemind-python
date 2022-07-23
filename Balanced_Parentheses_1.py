s=input()
s=list(s)
a=[]
for i in s:
    if i=='(' or i=='{' or i=='[':
        a.append(i)
    elif i==')':
        if a[-1]=='(':
            a.remove(a[-1])
    elif i==']':
        if a[-1]=='[':
            a.remove(a[-1])
    else:
        if a[-1]=='{':
            a.remove(a[-1])
if len(a)==0:
    print(True)
else:
    print(False)
    

    
