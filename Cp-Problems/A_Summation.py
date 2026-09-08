n=int(input())

p=list(map(int,input().split()))

total=0

for i in p:
  total = total+ i

if total<0:
  print(total*-1)
else:
  print(total)


















