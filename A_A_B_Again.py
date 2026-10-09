n=int(input())
while n>0:
    sum1=0
    y=int(input())
    e=[int(d) for d in str(y)]
    for i in e:
        sum1+=i
    print(sum1)
    n-=1
    
