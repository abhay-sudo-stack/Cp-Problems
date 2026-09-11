n=int(input())
fib1=0
fib2=1
fib=0
if n==1:
    print(fib1)
elif n==2:
    print(fib2)
else:
    for i in range(3,n+1):
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
    print(fib)



