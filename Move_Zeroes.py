
n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i==0:
        c.append(i)
    else:
        b.append(i)
print(*(b+c))
