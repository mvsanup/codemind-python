a=str(input())
v="aeiouAEIOU"
d=[]
for i in a:
    if i in v and  i not in d:
        d.append(i)
if(len(d)==0):
    print(-1)
else:
    print(*d)
        
