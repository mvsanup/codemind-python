n=int(input())
a=list(map(int,input().split()))
k=int(input())
d=[]
for i in a:
    if a.count(i)==k:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    d=set(d)
    d=list(d)
    print(*d)
    
    