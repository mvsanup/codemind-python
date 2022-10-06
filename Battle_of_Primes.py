def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n*0.5)+1):
        if(n%i==0):
            return 0
    return 1
a=int(input())
b=int(input())
d=a+b
k=d+1
while True:
    if(prime(k)):
        break
    k+=1
print(k-d)