x=int(input())
while x>0:
    y=int(input())
    z=[int(d) for d in str(y)]
    for i in z:
        print(i,end=" ")
    x-=1


