#program to find sum of squares
n=int(input("Enter a number: -"))
sm=0
for i in range(n+1):
    sq=i**2
    sm=sm+sq
    sq=0
print("Sum of the squares of numbers till {} is {}".format(n,sm))
    
