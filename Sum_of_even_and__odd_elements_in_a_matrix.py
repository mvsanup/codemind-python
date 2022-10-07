
r,c=map(int,input().split())
a=0
b=0
for i in range(r):
    k=list(map(int,input().split()))
    for i in k:
        if i%2==0:
            a+=i
        else:
            b+=i
print(a,b)
