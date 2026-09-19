x=list(map(int,input().split()))
y=x[0]
z=x[1]
count=0
while y<=z:
    y=y*3
    z=z*2
    count+=1

print(count)







