'''
#1. write a python code to reverse the string using for loop and slice operator
# Input string
city = "ETLQALabs"

# Reversing using for loop
reversed_for = ""
for char in city:
    reversed_for = char + reversed_for

# Reversing using slice operator
reversed_slice = city[::-1]

# Formatting the expected output
formatted_output = " ".join([reversed_slice[:3], reversed_slice[3:5], reversed_slice[5:]])

# Print results
print("Reversed using for loop:", reversed_for)
print("Reversed using slice operator:", reversed_slice)
print("Expected output:", formatted_output)


#2. Extract a substring form character "Q" and ends at "b"
# Input string
city = "ETLQALabs"

# Extract substring from 'Q' to 'b'
start_index = city.index("Q")  # Find the index of 'Q'
end_index = city.index("b")    # Find the index of 'b'
substring = city[start_index:end_index + 1]  # Include 'b' by adding 1 to the end index

# Output the result
print("Extracted substring:", substring)

#3. Write a python code to check if the given list contains duplicate elements and print yes or no as per input
# Function to check for duplicates
def contains_duplicates(input_list):
    # Convert list to set and compare lengths
    if len(input_list) != len(set(input_list)):
        return "Yes"
    else:
        return "No"

# Examples
list1 = [1, 2, 3, 4, 3]
list2 = [1, 2, 3, 4]

# Output results
print("List1 contains duplicates:", contains_duplicates(list1))  # Output: Yes
print("List2 contains duplicates:", contains_duplicates(list2))  # Output: No

#4. How would you use slicing to create a new list containing only the odd-indexed elements of a given list?
# Input list
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extracting odd-indexed elements using slicing
odd_indexed_elements = input_list[1::2]  # Start at index 1, step by 2

# Output the result
print("Odd-indexed elements:", odd_indexed_elements)

#5. How would you use slicing to create a new list containing only the even-indexed elements of a given list?
# Input list
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extracting odd-indexed elements using slicing
odd_indexed_elements = input_list[0::2]  # Start at index 1, step by 2

# Output the result
print("Odd-indexed elements:", odd_indexed_elements)
'''