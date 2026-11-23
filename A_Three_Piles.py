n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    x,y,z=l[0],l[1],l[2]
    if z==y+1 and y==x+1:
        print("YES")
    else:
        print("NO")
    