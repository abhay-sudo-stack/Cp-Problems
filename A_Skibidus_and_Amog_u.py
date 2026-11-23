n=int(input())
for i in range(n):
    s=list(input())
    if s[-2]=='u' and s[-1]=='s':
        s.pop(-2)
        s[-1]='i'
        cmb="".join(s)

    print(cmb)