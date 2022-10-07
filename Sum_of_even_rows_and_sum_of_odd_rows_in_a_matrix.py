r,c=map(int,input().split())
a=0
b=0
for i in range(r):
    k=list(map(int,input().split()))
    if i%2==0:
        a+=sum(k)
    else:
        b+=sum(k)
print(a,b)