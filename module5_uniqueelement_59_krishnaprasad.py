#UNIQUE ELEMENT IN LIST
lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input("enter your elements:")) 
    lst.append(ele)  
print("your previous list:",lst) 


lst2 = [] 

for x in lst: 
    if x not in lst2: 
        lst2.append(x) 
print("your new list:",lst2)
