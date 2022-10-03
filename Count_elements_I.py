n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
c=0
for i in a:
    if i in b and i not in d:
        d.append(i)
        c+=1
print(c)