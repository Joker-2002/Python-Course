import math
radius = int(input("enter the radius of th circle: "))

def circle(r):
    circumference = 2 * math.pi * r
    area = math.pi * r ** 2
    return format(circumference,'.3f'),format(area,'.3f')

circumference,area = circle(radius)
print(f"Circumference of circle is: {circumference}")
print(f"Area of the circle is: {area}")