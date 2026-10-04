n=int(input())
for i in range(n):
    y=list(map(int,input().split()))
    a=y[0]
    b=y[1]
    count1=0
    while a%b!=0:
        a+=1
        count1+=1
    print(count1)
 

