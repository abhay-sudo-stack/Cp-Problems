x=int(input())
y=int(input())
z=list(map(int,input().split()))
for i in range(1,y):
    for j in range(1,y):
            print(z[i]+z[j+i]+(j+1)-i)
            if i==y-1:
                print(z[i]+z[j]+)

        