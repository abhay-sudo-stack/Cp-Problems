a=input()
b=input()
c=[str(d) for d in a]
f=[str(e) for e in b]
if c[0]=="A" and f[0]=="D":
    print("Yes")
elif c[0]=="D" and f[0]=="A":
    print("Yes")
elif c[0]=="A" and c[1]=="D":
    print("Yes")
elif c[0]=="D" and c[1]=="A":
    print("Yes")
elif c[1]=="D" and f[1]=="A":
    print("Yes")
elif c[1]=="A" and f[1]=="D":
    print("Yes")
elif f[0]=="A" and f[1]=="D":
    print("Yes")
elif f[0]=="D" and f[1]=="A":
    print("Yes")
else:
    print("No")


