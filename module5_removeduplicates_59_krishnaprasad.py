#REMOVE CONSECUTIVE DUPLICATES FROM LIST
list = [1,1,1,1,1,1,2,3,4,4,5,1,2]
i = 0
dope = False

while i < len(list)-1:
    if list[i] == list[i+1]:
        del list[i]
        dope = True
    elif dope:
        del list[i]
        dope = False
    else:
        i += 1
print(list)
