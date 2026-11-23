n=int(input())
for i in range(n):
    l1=list(map(int,input().split()))
    if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]==l1[3]:
        print("YES")
    else:
        print("NO")