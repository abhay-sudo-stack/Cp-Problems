x=int(input())
while x>0:
    y=list(map(int,input().split()))
    t=y[0]
    r=y[1]
    u=y[2]
    if t+r==u:
        print("+")
    elif t-r==u:
        print("-")

    x-=1