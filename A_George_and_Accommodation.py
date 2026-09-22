x=int(input())
count=0
for i in range(1,x+1):
    y=list(map(int,input().split()))
    if y[1]-y[0]>=2:
        count+=1

print(count)

