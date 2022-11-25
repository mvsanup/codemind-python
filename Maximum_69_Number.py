a,n=int(input()),[]
while a:
    n.append(a%10)
    a//=10
for i in range(len(n)-1,-1,-1):
    if n[i]==6:
        n[i]=9
        break
print(*n[::-1],sep='')