print("Hi Pitchaimani Mani, Good Morning. Have a nice day!")
'''
order_status = {"closed", "completed", "processing", "closed"}
print(order_status)

#Adding and Removing Elements:
order_status.add("pending")
print(order_status)

mixed_set = {"closed", 1, 1.5, True, (1, 2, 3)}
print(mixed_set)

#invalid_set = {"closed", [1, 2, 3]}
#print(invalid_set) #TypeError: unhashable type: 'list'

order_status = {"closed", "completed", "processing", "closed"}
print(order_status)
print("closed" in order_status)
print("Closed" in order_status) 

numbers = [1, 2, 3, 3, 4, 3, 8, 7, 2]
unique_numbers = set(numbers)
print(unique_numbers)
'''

with open("sales_data.csv", "r") as file:
    next(file)  # Skip the header
    order_status_list = [line.strip().split(",")[0] for line in file]
order_status_set = set(order_status_list)
print(order_status_list)
print(order_status_set)
valid_numbers = {'5','3','2','1','4'}
invalid_numbers = order_status_set-valid_numbers
print(invalid_numbers)
