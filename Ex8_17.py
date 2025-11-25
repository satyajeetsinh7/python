import math

# a. Convert degree to radian
degree = 180
radian = math.radians(degree)
print(radian)

# b. Calculate y = 6x^2 + 4sin(x)
x = math.pi
y = 6 * (x**2) + 4 * math.sin(x)
print(y)

# c. Functions f(x), f'(x), f''(x)
def functions(x):
    f = math.cos(2*x)
    f1 = -2 * math.sin(2*x)
    f2 = -4 * math.cos(2*x)
    return f, f1, f2

result = functions(math.pi)
print(result)
