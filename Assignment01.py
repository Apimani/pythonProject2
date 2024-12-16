'''
#Write a function to return the grade based on percentage
def get_grade(percentage):
    """
    Returns the grade based on the percentage.

    Grading Criteria:
    - 90-100: A+
    - 80-89 : A
    - 70-79 : B
    - 60-69 : C
    - 50-59 : D
    - Below 50: F
    """
    if 90 <= percentage <= 100:
        return "A+"
    elif 80 <= percentage < 90:
        return "A"
    elif 70 <= percentage < 80:
        return "B"
    elif 60 <= percentage < 70:
        return "C"
    elif 50 <= percentage < 60:
        return "D"
    elif 0 <= percentage < 50:
        return "F"
    else:
        return "Invalid Percentage"  # Handles invalid inputs


# Input from the user
percentage = int(input("Enter the percentage number: "))

# Call the function and print the grade
grade = get_grade(percentage)
print(f"The grade for {percentage}% is: {grade}")

#Write a function that return a list of common elements from two different sets
def common_elements(set1, set2):
    """
    Returns a list of common elements from two sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        list: A list of common elements.
    """
    return list(set1.intersection(set2))

# Example usage
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
result = common_elements(set_a, set_b)
print(result)  # Output: [4, 5] (order may vary)


def findCommonElement(set1, set2):
    set3 = set1 & set2
    return set3
set1 = {1,2,3,4,5}
set2 = {1,4,5,8,9}
print(findCommonElement(set1,set2))


#Convert a String to a List of Characters
def string_to_list(input_string):
    """
    Converts a string to a list of characters.

    Args:
        input_string (str): The string to convert.

    Returns:
        list: A list of characters from the string.
    """
    return list(input_string)

# Example usage
text = "Hello, World!"
result = string_to_list(text)
print(result)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


def string_to_list_comprehension(input_string):
    """
    Converts a string to a list of characters using list comprehension.

    Args:
        input_string (str): The string to convert.

    Returns:
        list: A list of characters from the string.
    """
    return [char for char in input_string]

# Example usage
text = "Hello, World!"
result = string_to_list_comprehension(text)
print(result)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


def convertStringToList(s):
    return list(s)
s = input("Enter a string : ")
print(convertStringToList(s))


#Write a function to check if list contains any duplicate element and return True or False as applicable
def has_duplicates(input_list):
    """
    Checks if a list contains any duplicate elements.

    Args:
        input_list (list): The list to check.

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
    return len(input_list) != len(set(input_list))

# Example usage
example_list = [1, 2, 3, 4, 5, 6, 2]
print(has_duplicates(example_list))  # Output: True

example_list_no_duplicates = [1, 2, 3, 4, 5]
print(has_duplicates(example_list_no_duplicates))  # Output: False


def checkDuplicateInList(lst):
    set1 = set(lst)
    if(len(set1) == len(lst)):
        return False
    else:
        return True
lst = [1,2,3,4,5,13]
ans = checkDuplicateInList(lst)
print(ans)


#Given a list, write a function that provide the occurrence of element against each element in the list.
#e.g. List = [1,2,3,4,5,1,3]
def count_occurrences(input_list):
    """
    Counts the occurrences of each element in the list.

    Args:
        input_list (list): The list to process.

    Returns:
        dict: A dictionary with elements as keys and their occurrences as values.
    """
    occurrence_dict = {}
    for element in input_list:
        occurrence_dict[element] = occurrence_dict.get(element, 0) + 1
    return occurrence_dict

# Example usage
example_list = [1, 2, 3, 4, 5, 1, 3]
result = count_occurrences(example_list)
print(result)  # Output: {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}
'''


def substring_from_a_to_b(input_string):
    """
    Returns a substring that starts from the 2nd occurrence of 'a' and ends at the next occurrence of 'b'.

    Args:
        input_string (str): The string to process.

    Returns:
        str: The resulting substring, or an empty string if conditions are not met.
    """
    first_a_index = input_string.find('a')  # Find the first occurrence of 'a'
    second_a_index = input_string.find('a', first_a_index + 1)  # Find the second occurrence of 'a'

    if second_a_index == -1:  # No second occurrence of 'a'
        return ""

    b_index = input_string.find('b', second_a_index)  # Find the next 'b' after the second 'a'

    if b_index == -1:  # No 'b' found after the second 'a'
        return ""

    return input_string[second_a_index:b_index + 1]


# Example usage
s = "abracadabra"
result = substring_from_a_to_b(s)
print(result)  # Output: "acadab"

