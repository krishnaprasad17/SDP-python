#LONGEST WORD IN FILE
lst1=[]
with open("test.txt", "r") as f:
    f_contents = f.readline()
    lst1.append(f_contents)
    res = max(lst1, key = len) 
print(res)
