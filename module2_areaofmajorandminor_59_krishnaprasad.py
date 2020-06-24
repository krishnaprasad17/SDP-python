import math
pi=3.14
def area_of_segment(radius,angle):
    area_of_sector=pi*(radius*radius)*(angle/360)
    area_of_triangle=1/2*(radius*radius)*math.sin((angle))
    return area_of_sector - area_of_triangle;

radius=10.0
angle=90.0
print("area of minor segment=",area_of_segment(radius,angle))
print("area major segment=",area_of_segment(radius,(360-angle)))
