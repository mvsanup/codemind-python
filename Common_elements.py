m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
for i in a:
    if i in b and i not in d:
        d.append(i)
print(*d)