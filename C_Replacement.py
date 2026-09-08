x = int(input())
y = list(map(int,input().split()))

for i in range(len(y)):
    if y[i]>0:
        y[i]=1
    if y[i]<0:
        y[i]=2
    if y[i]==0:
        y[i]=0

for i in y:
    print(i,end=" ")
