a=str(input())
a=a.lower()
b=[]
for i in a:
    if a.count(i)==1 :
        b.append(i)
if ' ' in b:
    b.remove(' ')
b.sort()
print(len(b))