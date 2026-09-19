x=int(input())
z=[]
while x>0:
    y=list(map(int,input().split()))
    for i in y:
        for j in str(i):
            z.append(j)
            z.reverse()



    x-=1

