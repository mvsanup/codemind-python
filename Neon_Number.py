n=int(input())
a=n*n
b=a
sum=0
while a:
    d=a%10
    sum+=d
    a=a//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    
    