n=int(input())
count2=0
for i in range(n):
    L1=list(map(int,input().split()))
    count1=0
    for i in L1:
        if i==1:
            count1+=1

    if count1>=2:
        count2+=1

print(count2)
    