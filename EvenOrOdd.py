a=[1,2,3,4,5,6,7,8,9,10]
b=0
c=0
while b<10:
    d=(a[c])%2
    if c==0:
        if d==0:
            print("The 1st term of list A is even.")
        else:
            print("The 1st term of list A is odd.")
    elif c==1:
        if d==0:
            print("The 2nd term of list A is even.")
        else:
            print("The 2nd term of list A is odd.")
    elif c==2:
        if d==0:
            print("The 3rd term of list A is even.")
        else:
            print("The 3rd term of list A is odd.")
    else:
        if d==0:
            print("The "+str(c)+"th term of list A is even.")
        else:
            print("The "+str(c)+"th term of list A is odd.")
    b=b+1
    c=c+1
    

        
