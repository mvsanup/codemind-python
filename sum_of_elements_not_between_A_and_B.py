n=int(input())
a=list(map(int,input().split()))
b,d=map(int,input().split())
m=[]
for i in a:
    if  i<b or i>d:
        m.append(i)
print(sum(m))
        
