#CONVERT LINES OF FILE INTO LIST
lst1=[ ]
with open("test.txt", "r") as f:
    f_contents = f.readline()
    lst1.append(f_contents)
    print(lst1)
