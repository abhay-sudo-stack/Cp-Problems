x=int(input())
y=list(map(int,input().split()))
count1=0
count2=0
for i in y:
    if i==1:
        count1=count1+1

if count1>=1:
    print("HARD")
if count1==0:
    print("EASY")