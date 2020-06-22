# program to find max of three numbers
def mx(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest
if __name__ =="__main__":
    num1=float(input("Enter the value of num1: - "))
    num2=float(input("Enter the value of num2: - "))
    num3=float(input("Enter the value of num3: - "))
    maxi=mx(num1,num2,num3)
    print("The largest of {}, {}, {} is :- {}".format(num1,num2,num2,maxi))
    
