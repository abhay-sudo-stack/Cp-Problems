x=int(input())
y=list(map(int,input().split()))

for i in range(len(y)):
    if y[i]<=10:
        print("A[",i,"] = ",y[i],sep="")

