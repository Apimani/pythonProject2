'''
# Define course fees
big_data_fee = 800
azure_fee = 600
# Number of enrollments
big_data_enrollments = 20
azure_enrollments = 40
# Calculate total revenue
total_revenue = (big_data_fee * big_data_enrollments) + (azure_fee * azure_enrollments)
print(f"Total revenue: ${total_revenue} USD")

result_add = 5 + 3 * 8  # Expected: 29 because multiplication has higher precedence
print(result_add)

result_parentheses = (5 + 3) * 8  # Expected: 64
print(result_parentheses)

result_div = 15 / 4  # Expected: 3.75
result_int_div = 15 // 4  # Expected: 3
print(result_div)
print(result_int_div)

result_mod = 15 % 4  # Expected: 3
result_exp = 2 ** 3  # Expected: 8
print(result_mod)
print(result_exp)

import math
# Ceiling and floor functions
total_sales = 20000.60
print(math.ceil(total_sales))  # Expected: 20001
print(math.floor(total_sales))  # Expected: 20000
# Absolute value function
negative_value = -20000.60
print(math.fabs(negative_value))  # Expected: 20000.60

# Determine grade based on marks
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade: A")
elif marks >=60:
    print("Grade: B")
elif marks >=45:
    print("Grade: C")
elif marks >= 35:
    print("You passed and get grade C1.")
else:
    print("You failed.")

# Check eligibility to vote based on age and criminal record
age = int(input("Enter your age: "))
has_criminal_record = input("Do you have a criminal record? (yes/no): ")
if age >= 18 and has_criminal_record.lower() == "no":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

condition1 = True
condition2 = False
result = condition1 or condition2
print(result)

# Take input from the user
age = int(input("Please enter your age: "))
crime_record = input("Are there any criminal records against you? (yes or no): ")
# Check if the user is eligible to vote
if age >= 18 and crime_record.lower() == "no":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

age = int(input("Please enter your age: "))
if not age < 18:
    print("You are eligible to vote.")

# Single quotes
name = 'Pitchaimani'
# Double quotes
name1 = "Pitchaimani"
# Triple quotes (used for multi-line strings)
name2 = 'Pitchaimani
is learning
Python'
print(name2)

text = "Sumit's class is \"really good\".\tHe teaches Python."
print(text)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Your full name is:", full_name)

name = input("Enter your name: ")
length = len(name)
print("The length of the name is:", length)

name = input("Enter your name: ")
print(name[0])  # Output:
print(name[-1]) # Output:

order_status = "Complete Order"
print(order_status[::-1])  # Output: Complete

string = "complete order"
print(string[:7])
print(string[9:14])
length = len(string)
print(string[9:length])
print(string[9:])
print(string[:8])
print(string[:])
print(string[-5:])
index = string.find(" ")
print(string[index + 1:])
print(string[:index])
print(string.find("e"))
print(string.find("z"))
print(string.index("e"))
print(string.endswith("order"))
print(string.capitalize())

string_with_spaces = "  complete order  "
print(string_with_spaces)
print(string_with_spaces.strip())

string = "complete order"
print(string)
print(string.replace("complete", "Pitchaimani"))
'''
order_details = "order_id, timestamp, customer_id, order_status"
order_details_list = order_details.split(", ")
print(order_details_list)
print(order_details_list[3])
order_status = order_details_list[3].strip()
order_status = order_status.upper()
print(order_status)








