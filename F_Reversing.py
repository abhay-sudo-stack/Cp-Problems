x=int(input())
y= list(map(int,input().split()))

y=y[::-1]
for i in y:
    print(i,end=" ")