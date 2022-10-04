m,n=map(int,input().split())
b=list(map(int,input().split()))
c=0
for i in b:
    if i%n==0:
        c+=1
print(c)