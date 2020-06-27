#APPENDING IN MIDDLE
s1=input("enter string 1 :")
s2=input("enter string 2 :")

a=(len(s1)//2)

str=s1[:a]+s2+s1[a:]
print(str)
