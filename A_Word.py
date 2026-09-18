x=input()
countu=0
countl=0
for i in x:
    if str.isupper(i)==True:
        countu+=1
    elif str.islower(i)==True:
        countl+=1

if countu>countl:
    print(x.upper())
elif countl>countu:
    print(x.lower())
elif countl==countu:
    print(x.lower())
