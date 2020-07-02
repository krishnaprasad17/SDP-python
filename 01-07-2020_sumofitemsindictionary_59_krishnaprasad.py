#SUM OF ALL THE ITEMS IN DICTIONARY
a=[]
my_dict = {'data1':100,'data2':-54,'data3':247}
a=list((my_dict.values()))
sum=0
for i in a:
    sum+=i    
print(a)
print(sum)
