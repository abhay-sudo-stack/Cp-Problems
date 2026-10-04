n=int(input())
z=[]
for i in range(n):
    x=int(input())
    if x%3!=0:
        z.append(x)

for i in z:
   s = [int(d) for d in str(i)]
   if s[-1]!=3:
       print(s[-1])
1   



          
