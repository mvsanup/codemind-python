r,c=map(int,input().split())
a=[]
x=[]
for i in range(r):
    a.append(list(map(int,input().split())))
for i in range(c):
    s=0
    for j in range(r):
        s+=a[j][i]
    x.append(s)
print(max(x))