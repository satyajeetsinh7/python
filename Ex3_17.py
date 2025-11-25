# a. Write a Python program to reverse a string.
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# b. Write a Python program to check if a string is a palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# c. Write a Python program to check if a string contains only digits.
s = input("Enter a string: ")
if s.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")

# d. Write a Python program to find the longest word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

# e. Write a Python program to find the length of the last word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Length of last word:", len(words[-1]))
