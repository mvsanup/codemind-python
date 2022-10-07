n=int(input())
a=0
b=1
for i in range(n+1):
   c=a+b
   b=a
   a=c
   if c==n:
       print(True)
       break
else:
    print(False)