from math import tan,pi
n_sides=int(input("input number of sides:"))
s_length=float(input("input the length of side:"))
p_area=n_sides*(s_length**2)/(4*tan(pi/n_sides))
print("the area of polygon is:",p_area)
