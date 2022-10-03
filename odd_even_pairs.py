n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)
for i in range(min(len(b),len(c))):
    print(c[i],b[i],end=" ")
if(len(b)>len(c)):
    for i in range(len(c),len(b)):
        print(b[i],end=" ")
if(len(c)>len(b)):
    for i in range(len(b),len(c)):
        print(c[i],end=" ")
if(n%2):
    print(0)