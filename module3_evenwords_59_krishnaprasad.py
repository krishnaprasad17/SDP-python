#PRINT EVEN WORDS
d=input("enter the string :")

words = d.split() 
j=0
for i in words:
    if(len(words[j])%2==0):
        print("word's are :",i)
        j=j+1
