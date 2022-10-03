n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
c=0
for i in a:
    if i not in b:
        d.append(i)
for i in b:
    if i not in a and i not in d:
        d.append(i)
print(*d)