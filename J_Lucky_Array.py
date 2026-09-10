#Code using Functions
x=int(input())
y=list(map(int,input().split()))

z=min(y)
a=y.count(z)

if a%2==0:
    print("Unlucky")
else:
    print("Lucky")

#Code using Loops

x=int(input())
y=list(map(int,input().split()))
count=0
for i in range(0,len(y)-1):
    for j in range(0,len(y)-1):
        temp=y[j]
        if y[j]>y[j+1]:
            y[j]=y[j+1]
            y[j+1]=temp

z=y[0]
for i in y:
    if z==i:
        count+=1

if count%2==0:
    print("Unlucky")
else:
    print("Lucky")






