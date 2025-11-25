# Write a Python program to Count the occurrences of an element in a tuple.
numbers = (1, 2, 3, 4, 2, 5, 2, 6, 7, 2, 8)
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element {element} occurs {count} times in the tuple.")

# Write a Python program to Check if an element exists in a tuple.

numbers = (10, 20, 30, 40, 50)
element = int(input("Enter the element to search: "))
if element in numbers:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# Write a Python program to Convert a tuple to a string.

t = ('P', 'y', 't', 'h', 'o', 'n')
s = ''.join(t)
print("Converted string:", s)

# Write a Python program to Find the maximum and minimum elements in a tuple.
t = (5, 9, 1, 7, 3, 8)
print("Maximum:", max(t))
print("Minimum:", min(t))

# Write a Python program to convert a tuple of strings to a single string.
t = ('Hello', 'World', 'Python')
s = ' '.join(t)
print("Single string:", s)

# Write a Python program to sort a tuple of integers.

t = (7, 2, 9, 1, 5)
sorted_tuple = tuple(sorted(t))
print("Sorted tuple:", sorted_tuple)

# Write a python program to find the first and last elements of a tuple.
t = (10, 20, 30, 40, 50)
print("First element:", t[0])
print("Last element:", t[-1])