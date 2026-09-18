x=list(map(int,input().split()))
z=x[1]
y=x[0]
r=0
f=0
for i in range(1,z+1):
    if y%10==0:
        r=y%10
        y=r
    else:
        y=y-i
        
print(y)