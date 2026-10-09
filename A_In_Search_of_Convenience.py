n=int(input())
while n>0:
    a=list(map(int,input().split()))
    x=a[0]
    y=a[1]
    r=a[2]
    print(x,y+r)
    n-=1
    