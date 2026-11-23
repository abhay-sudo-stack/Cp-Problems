n=int(input())
y=list(map(int,input().split()))
sum1=0
for i in range(0,n):
    if i%2==0:
        sum1+=y[i]

print(sum1)