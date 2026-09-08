x= int(input())
y= list(map(int,input().split()))
t=0
for i in y:
    t=min(y)
    print(t,end=" ")
    if t==i:
        print(1-(y.index(i)))
    break

    