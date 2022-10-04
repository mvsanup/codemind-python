a=str(input())
v="aeiou"
a=a.lower()
d=[]
for i in v:
    if i not in a:
        d.append(i)
d.sort()
if(len(d)==0):
    print(0)
else:
    print(*d)