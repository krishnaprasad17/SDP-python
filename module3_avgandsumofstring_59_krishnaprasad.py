#RETURN AVERAGE AND SUM OF DIGITS IN STRING
try:   
            num=int(input("enter a number :"))
            i=0
            sum=0
            num1=num
            while(num>0):
                i=i+1
                rem=num%10
                sum+=rem
                num=num//10
            print("sum:",sum)
            print("average :",sum/i)
except:
        print("please enter valid input..!!")
finally:
        print("THANK YOU...!!")
