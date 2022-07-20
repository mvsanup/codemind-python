n=int(input())
a=list(map(int,input().split()))
y=[]
for i in a:
    if a.count(i)>=1 and i not in y:
        print(i,end=' ')
        y.append(i)
