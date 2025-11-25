# a. Multiply all the items in a list
numbers = [2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print(result)

# b. Get the largest number from a list
numbers = [2, 45, 23, 89, 10]
print(max(numbers))

# c. Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
print(list(set(numbers)))

# d. Get the frequency of elements in a list
numbers = [1, 2, 2, 3, 4, 4, 5]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
print(freq)

# e. Find common items from two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list(set(list1) & set(list2)))

# f. Convert a list of multiple integers into a single integer
numbers = [1, 2, 3, 4]
print(int("".join(map(str, numbers))))
