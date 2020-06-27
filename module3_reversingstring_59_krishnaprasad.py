#REVERSE WORDS IN STRING
e=input("enter the string :")

words = e.split() 

for i in words:
    print("",words[::-1])
