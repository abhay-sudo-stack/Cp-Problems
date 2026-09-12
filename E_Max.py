x=int(input())
y=list(map(int,input().split()))
for i in range(0,len(y)-1):
    for j in range(0,len(y)-1):
        if y[j]>y[j+1]:
            temp=y[j]
            y[j]=y[j+1]
            y[j+1]=temp

print(y[-1])

