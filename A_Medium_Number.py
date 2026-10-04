n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    c=max(x)
    y=min(x)
    x.remove(c)
    x.remove(y)
    for i in x:
        print(i)