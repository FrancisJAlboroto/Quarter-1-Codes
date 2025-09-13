import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x = pow((x2 - x1), 2)
y = pow((y2 - y1), 2)
distance = math.sqrt(x + y)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")