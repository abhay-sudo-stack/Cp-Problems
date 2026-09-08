x= int(input()) 
y=list(map(int,input().split()))
z= int(input())

for i in range(len(y)):
    if y[i]==z:
        print(i)
        break
if y[i]!=z:
    print(-1)
    
