n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
m=[]
for i in a:
    if i<x or i>y:
        m.append(i)
if len(m)==0:
    print(-1)
    
print(max(m))