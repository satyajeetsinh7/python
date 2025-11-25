# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np
x = np.arange(2, 11).reshape(3, 3)
print(x)

# Write a NumPy program to reverse an array (the first element becomes the last).

x = np.array([1, 2, 3, 4, 5])
print(x[::-1])

# Write a NumPy program to find common values between two arrays.

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
print(np.intersect1d(a, b))

# Write a NumPy program to repeat array elements.

x = np.array([1, 2, 3])
print(np.repeat(x, 3))

# Write a NumPy program to find the memory size of a NumPy array.

x = np.array([10, 20, 30, 40, 50])
print("%d bytes" % (x.size * x.itemsize))

# Write a NumPy program to create an array of ones and zeros.

print(np.ones((3,3)))
print(np.zeros((3,3)))

# Write a NumPy program to find the 4th element of a specified arr
x = np.array([10, 20, 30, 40, 50, 60])
print(x[3])