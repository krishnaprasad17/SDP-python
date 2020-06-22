#take three inputs from user and check
#all are equal
#any of two are equal
print("first number:")
first=input()
print("second number:")
second=input()
print("third number:")
third=input()
all = first == second and second == third and third == first
print("all are equal:",all)
any = first == second or second == third == first
print("any two are equal:",any)
      
