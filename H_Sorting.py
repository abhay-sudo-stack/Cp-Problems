x=int(input())
list2=list(map(int,input().split()))
for i in range(0,len(list2)-1):
    for j in range(0,len(list2)-1):
        if list2[j]>list2[j+1]:
            temp=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=temp

for i in list2:
    print(i,end=" ")

