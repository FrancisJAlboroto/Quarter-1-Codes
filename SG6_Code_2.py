import math  

PI = math.pi  
PI_3SIG = round(math.pi, 2)  # 3 significant digits: 3.14

radius = float(input("Enter the radius of the circle: "))  
area = PI_3SIG * radius ** 2  

print(f"The area of the circle with radius {radius} is {area}")  
