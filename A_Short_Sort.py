x=int(input())
h=['a','b','c']
    
for i in range(x):
    y=list(input())
    if y!=h:
        y[0],y[1]=y[1],y[0]
        if y==h:
            print("YES")
        else:
            y[0],y[1]=y[1],y[0]
            if y==h:
                print("YES")
            else:
                print("NO")
    else:
        print("YES")

        


    