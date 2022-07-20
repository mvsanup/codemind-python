n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
y=[]
for i in a:
    if i<b or i>c:
        y.append(i)
if len(y)==0:
    print(-1)
print(min(y))