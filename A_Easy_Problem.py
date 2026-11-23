x=int(input())
for i in range(x):
    n=int(input())
    a=n-1
    b=1
    cnt1=0
    while a>0 and b<n:
        a-=1
        b+=1
        cnt1+=1

    print(cnt1)
    