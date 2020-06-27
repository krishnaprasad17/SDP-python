#COUNT THE NUMBER OF VOWELS IN STRING
a=input("enter your string :")

vowels='aeiou'
count=0
for s in a:
    if s in vowels:
        count=count+1
print("",count)
