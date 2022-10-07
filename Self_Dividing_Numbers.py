def fun(n):
    c=0
    count=0
    temp=n
    while n:
        d=n%10
        if d==0:
            return 0
        if (temp%d==0):
            c+=1
        count+=1
        n=n//10
    if c==count:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(fun(i)):
        print(i,end=' ')