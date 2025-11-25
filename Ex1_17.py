# a. Write a program that displays “Welcome to Python” five times.
for i in range(5):
    print("Welcome to Python")

# b. Write a program that displays the following table:
# a   a^2   a^3
# 1    1     1
# 2    4     8
# 3    9    27
# 4   16    64
print("a\t a^2\t a^3")
for a in range(1, 5):
    print(a, "\t", a**2, "\t", a**3)

# c. Write a program that displays the result of
# (9.5 × 4.5 – 2.5 × 3) / (45.5 – 3.5)
result = (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5)
print(result)
