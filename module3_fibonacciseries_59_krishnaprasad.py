#program to find fibonacci series
n=int(input("enter how many numbers you want in series:"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second
