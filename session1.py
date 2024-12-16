print('Hello, Mr.Pitchaimani Mani, Good Morning. Have a nice day!')
'''
print("Hello, Data Engineers")

print("Hello World")

instructor_name = "Pitchaimani M"
course_fee = 800
course_rating = 4.95
is_starting_soon = True
total_income = None

print(type(instructor_name))  # Output: <class 'str'>
print(type(course_fee))       # Output: <class 'int'>
print(type(course_rating))    # Output: <class 'float'>
print(type(is_starting_soon)) # Output: <class 'bool'>
print(type(total_income))     # Output: <class 'NoneType'>

course_fee = 800
course_fee += 50
print(course_fee)

course_fee = "800"
course_fee = int(course_fee) + int(course_fee) * 0.1
print(course_fee)  # Output: 880.0

first_name = "Pitchaimani"
last_name = "Mani"
full_name = first_name + " " + last_name
print(full_name)

full_name = "Pitchaimani" + " " + "Mani"
print(full_name)

first_name = "Pitchaimani"
last_name = "Mani"
print("My first name is " + first_name + " and my last name is " + last_name)

first_name = "Pitchaimani"
last_name = "Mani"
print(f"My first name is {first_name} and my last name is {last_name}")

print("All is Well  " * 6)

first_name = "Pitchaimani"
last_name = "Mani"
for i in range(6):
    print(f"My first name is {first_name} and my last name is {last_name}")
'''

#salary = input("What is your current salary? ")
#hike_percentage = input("What is the hike percentage? ")

salary = int(input("What is your current salary? "))
hike_percentage = int(input("What is the hike percentage? "))
new_salary = salary + (salary * hike_percentage / 100)
print(f"The new salary after the hike is {new_salary}")

