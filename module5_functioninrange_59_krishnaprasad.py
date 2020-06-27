#FUNCTION TO CHECK NUMBER IS IN RANGE
def check():
    a=int(input("enter value to check:"))
    b=int(input("enter the minimum range:"))
    c=int(input("enter the maximum range:"))
    j=0
    for i in range(b,c+1):
        if(i==a):
            j=1
            break
        else:
            j=0
          
    if(j==1):
        print("Yes..its in!")
    else:
        print("Nope..not in range!")
