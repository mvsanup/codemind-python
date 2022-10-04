r,c=map(int,input().split())
s=0
for i in range(r):
    a=list(map(int,input().split()))
    s+=(sum(a))
print(s)