t=int(input())
for i in range(t):
    n=list(map(int,input().split()))
    n.sort()
    x,y=n[0],n[1]
    z=[]
    for i in range(x,y+1):
        if i!=x and i!=y:
            if i%2!=0:
                z.append(i)
    
    print(sum(z))



