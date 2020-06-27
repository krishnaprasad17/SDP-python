#CALCULATE NUMBER OF UPPER AND LOWER CASES
def cnt():
    
    s1=input("enter a string :").strip()
    count=0
    countu=0
    for i in s1:
        if(i.islower()):
            count+=1
            
        elif(i.isupper()):
            countu+=1
            
        else:
            pass
    print("THE NUMBER OF UPPER CASES ARE :",countu)
    print("THE NUMBER OF LOWER CASSES ARE: ",count)
    cnt()
