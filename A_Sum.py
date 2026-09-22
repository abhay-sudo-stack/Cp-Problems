x=int(input())
while x>0:
    y=list(map(int,input().split()))
    if y[0]==y[1]+y[2]:
        print("YES")
    elif y[1]==y[0]+y[2]:
        print("YES")
    elif y[2]==y[0]+y[1]:
        print("YES")
    else:
        print("NO")
    x-=1