h=int(input())
f=[]
for i in range(h):
    t=list(map(int,input().split()))
    a=t[0]
    b=t[1]
    for i in range(a,b+1):
        c=i
        z=(c-a)+(b-c)
        f.append(z)

    print(min(f))





