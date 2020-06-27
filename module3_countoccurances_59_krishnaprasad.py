#COUNT OCCURENCES OF CHARS
a=input("enter a string :")

b=a.strip().lower()

   
all_freq = {} 
 
for i in b: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  

print("Count of all characters is :\n "+  str(all_freq))
