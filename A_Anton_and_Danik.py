x=int(input())
y=input()
z=list(y)
count1=0
count2=0
for i in z:
    if i=="D":
        count1+=1
    if i=="A":
        count2+=1

if count1>count2:
    print("Danik")
if count2>count1:
    print("Anton")
if count1==count2:
    print("Friendship")