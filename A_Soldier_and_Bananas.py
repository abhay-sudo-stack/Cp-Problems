
# 546A Code Forces Akarisa

b=input()

L=[int(x) for x in b.split()]
a=0
c=0
d=0
t=0

for i in L:
  i[0]=a
  i[1]=c
  i[2]=d    

t=a*d

print(c-t)
