# a. Print all odd numbers between 1 to 100 using a while loop
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print()

# b. Find the sum of all natural numbers between 1 to n
n = 10
total = n * (n + 1) // 2
print(total)

# c. Count the number of digits in a number
num = 12345
print(len(str(num)))

# d. Find the first and last digits of a number
num = 12345
s = str(num)
print(s[0], s[-1])

# e. Swap the first and last digits of a number
num = 12345
s = str(num)
swapped = s[-1] + s[1:-1] + s[0] if len(s) > 1 else s
print(swapped)

# f. Calculate the product of digits of a number
num = 1234
product = 1
for digit in str(num):
    product *= int(digit)
print(product)

# g. Enter a number and print its reverse
num = 12345
reverse = str(num)[::-1]
print(reverse)
