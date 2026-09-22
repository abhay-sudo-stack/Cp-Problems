x=int(input())
n=0
while x>0:
    y=int(input())
    if y<=1399:
        print("Division 4")
    else:
        if y in range(1400,1600):
            print("Division 3")
        elif y in range(1600,1900):
            print("Division 2")
        elif y>=1900:
            print("Division 1")
    x-=1

 