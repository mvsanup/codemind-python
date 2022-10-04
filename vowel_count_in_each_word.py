a=str(input())
a=a.split(' ')
v="aeiou"

x=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    x.append(c)
print(*x)

        