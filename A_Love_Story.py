

n=int(input())
l1=["c","o","d","e","f","o","r","c","e","s"]
cnt1=0
for i in range(n):
    s=list(input())
    for j in range(0,10):
        if l1[j]==s[j]:
            cnt1+=1
            
    print(cnt1)      