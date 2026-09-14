x=int(input())
count=0
z=[]
for i in range(1,x+1):
    if x%i==0:
        z.append(i)
if len(z)>2:
    print("NO")
else:
    print("YES")

