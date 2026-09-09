x= int(input())
y= list(map(int,input().split()))
t=0
for i in y:
    t=min(y)
    if t==i:
        print(t,y.index(i)+1)
        break

    