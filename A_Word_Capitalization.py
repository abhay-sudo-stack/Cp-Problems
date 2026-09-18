x=input()
l=[]

if x[0].islower()==True:
    l[0]=x[0].upper()

for i in x[1:]:
    if x[i].islower()==True:
        l[i]=x[i].upper()

if x[0].islower()==True:
    l[0]=x[0].upper()

print(l)

