n=int(input())
for i in range(n):
    l2=[]
    l1=list(map(int,input().split()))
    a=l1[0]
    b=l1[1]
    for j in range(a,b+1):
        l2.append(j)

    y=sum(l2)
    if y in l2:
        print(0)
    


