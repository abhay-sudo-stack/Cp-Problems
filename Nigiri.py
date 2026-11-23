s=list(input())
cnt1=0
for i in s:
    if i=="o":
        cnt1+=1

if cnt1%2==0:
    print("even")
else:
    print("odd")