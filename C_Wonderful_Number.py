s=int(input())

if s%2!=0:
    t=list(bin(s)[2:]) 
    y=t[::-1]
    if y==t:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
