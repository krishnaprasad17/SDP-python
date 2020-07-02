#SUM ALL THE ITEMS IN A LIST
a=[]
sum=0
b=int(input("number of elements??:"))
for i in range(b):
    c=int(input("enter elements into list :"))
    a.append(c)
    sum+=c
    
print(a)
print(sum)
