# Write a python code for calculating the Area and Perimeter of a Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# Write a python code for testing if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a python code for calculate the area and volume of the Cube.
side = float(input("Enter side of cube: "))
area_cube = 6 * (side ** 2)
volume_cube = side ** 3
print("Area of Cube:", area_cube)
print("Volume of Cube:", volume_cube)

# Write a python code to solve the equation z = (x+y)*(x-y)
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = (x + y) * (x - y)
print("z =", z)

# Write a python code to solve the equation z = (x+y)*(x+y)-2xy; write a comment on it.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = (x + y) * (x + y) - 2 * x * y
print("z =", z)
# This simplifies to x^2 + 2xy + y^2 - 2xy = x^2 + y^2

# Write a python code for Converting Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
