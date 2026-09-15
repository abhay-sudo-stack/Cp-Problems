import copy

x=int(input())
y=list(map(int,input().split()))
z=copy.copy(y)
for i in range(0,len(y)-1):
    for j in range(0,len(y)-1):
        if y[j]>y[j+1]:
            temp=y[j+1]
            y[j+1]=y[j]
            y[j]=temp

F=y[0]
G=y[-1]

for i in z:
    if i==F:
        ind_small=z.index(i)
    if i==G:
        ind_big=z.index(i)

z[ind_small]=G
z[ind_big]=F

for i in z:
    print(i,end=" ")
