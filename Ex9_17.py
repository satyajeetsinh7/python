import pandas as pd

# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

print("Add two Series:")
print(s1 + s2)

print("\nSubtract two Series:")
print(s1 - s2)

print("\nMultiply two Series:")
print(s1 * s2)

print("\nDivide two Series:")
print(s1 / s2)

# Write a Pandas program to convert a dictionary to a Pandas series.
py_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

print("Original dictionary:")
print(py_dict)

new_series = pd.Series(py_dict)

print("\nConverted series:")
print(new_series)

# Write a Pandas program to create a series from a list, numpy array and dict
import pandas as pd
import numpy as np

# From a list
py_list = [2, 4, 6, 8, 10]
series_from_list = pd.Series(py_list)
print("Series from list:")
print(series_from_list)

# From a NumPy array
np_array = np.array([2, 4, 6, 8, 10])
series_from_array = pd.Series(np_array)
print("\nSeries from NumPy array:")
print(series_from_array)

# From a dictionary
py_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(py_dict)
print("\nSeries from dictionary:")
print(series_from_dict)

# Write a Pandas program to stack two series vertically and horizontally
import pandas as pd

s1 = pd.Series(['p', 'q', 'r', 's'], name='Series1')
s2 = pd.Series([1, 2, 3, 4], name='Series2')

# Vertical stacking
vertical_stack = pd.concat([s1, s2])
print("Vertically stacked series:")
print(vertical_stack)

# Horizontal stacking
horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontally stacked series (as a DataFrame):")
print(horizontal_stack)