
n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i==1:
        c+=1
    else:
        b.append(c)
        c=0
b.append(c)
print(max(b))
