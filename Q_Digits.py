x=int(input())
while x>0:
    y=int(input())
    z=[int(d) for d in str(y)]
    z=z[::-1]
    for i in z:
        print(i,end=" ")

    print()
    x-=1


