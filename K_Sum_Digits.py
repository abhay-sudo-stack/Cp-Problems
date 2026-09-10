x=int(input())
y=list(map(int,input()))
z=[]
add1=0
for i in y:
    for j in str(i):
        z.append(j)

for d in z:
    add1=add1+int(d)

print(add1)
