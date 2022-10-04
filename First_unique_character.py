a=str(input())
a=a.lower()
for i in a:
    if a.count(i)==1:
        if i==' ':
            continue
        print(i)
        break
else:
    print(-1)