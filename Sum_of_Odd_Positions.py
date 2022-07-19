n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(n):
    if i%2:
        b+=a[i]
print(b)
    
        
        