n=int(input())
for i in range(n):
    s=list(input())
    temp=s[0]
    s[0]=s[4]
    s[4]=temp
    result = "".join(s[:3]) + "" + "".join(s[3:])
    print(result)