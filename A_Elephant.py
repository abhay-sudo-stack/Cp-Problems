x=int(input())
z=0

if x<=5:
    print(1)
if x>5:
    z=x//5
    if x%5==0:
        print(z)
    if x%5!=0:
        print(z+1)