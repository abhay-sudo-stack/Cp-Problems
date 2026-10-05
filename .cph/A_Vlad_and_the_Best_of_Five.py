n=int(input())

for i in range(n):
    count1=0
    count2=0
    x=list(input())
    
    for i in x:
        if i=="A":
            count1+=1
        elif i=="B":
            count2+=1

    if count1>count2:
        print("A")
    elif count1<count2:
        print("B")

    