a=int(input())
a=str(a)
a=list(a)
for i in a:
    if a.count(i)>1:
        print('Not Unique Number') 
        break
else:
    print('Unique Number')