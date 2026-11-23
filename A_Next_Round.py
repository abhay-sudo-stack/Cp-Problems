l=list(map(int,input().split()))
L1=list(map(int,input().split()))
n=l[1]
a=L1[n-1]
count1=0
for i in L1:
    if i>=a and i>0:
        count1+=1

print(count1)