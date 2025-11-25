import re

# Regex patterns
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Taking PAN number input
pan = input("Enter PAN card number: ")

# Taking Email ID input
email = input("Enter Email ID: ")

# PAN Validation
if re.match(pan_pattern, pan):
    print("Valid PAN number.")
else:
    print("Invalid PAN number.")

# Email Validation
if re.match(email_pattern, email):
    print("Valid Email ID.")
else:
    print("Invalid Email ID.")
