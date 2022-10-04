r,c=map(int,input().split())
x=[]
for i in range(r):
    a=list(map(int,input().split()))
    x.append(sum(a))
print(max(x))