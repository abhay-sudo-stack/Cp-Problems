x=int(input())
y=list(map(int,input().split()))
even=0
negative=0
positive=0
odd=0
for i in y:
    if i<0:
        negative+=1
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1

    elif i>0:
        positive+=1
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1
  
for i in y:
    if i==0:
        even+=1

print("Even:",even)
print("Odd:",odd)
print("Positive:",positive)
print("Negative:",negative)