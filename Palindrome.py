n=int(input())
r=0
k=n
while n:
    d=n%10
    r=r*10+d
    n=n//10
if(k==r):
    print("True")
else:
    print("False")