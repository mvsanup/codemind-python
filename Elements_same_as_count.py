n=int(input())
a=list(map(int,input().split()))
y=[]
for i in a:
    if i==a.count(i) and i not in y:
        y.append(i)
if len(y)==0:
    print(-1)
else:
    print(*y)