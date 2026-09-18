x=list(map(int,input().split()))
z=x[1]
y=x[0]
r=0
f=0
digits = [int(d) for d in str(y)]
if digits[-1]==0:
    del digits[-1]

