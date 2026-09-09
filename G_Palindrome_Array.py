x=int(input())
y=list(map(int,input().split()))

y1=y[::-1]

if y==y1:
    print("YES")
else:
    print("NO")
    