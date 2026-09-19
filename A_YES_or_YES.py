x=int(input())
L=[]

while x>0:
    y=input()
    L.append(y)
    x-=1

for i in L:
    r=i.lower()
    if r=="yes":
        print("YES")
    else:
        print("NO")
