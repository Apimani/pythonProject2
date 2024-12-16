print("Hi Pitchaimani Mani, Good Morning. Have a nice day!")
'''
#list
orders = [1, "2013-07-25 00:00:00.0", 11599, "CLOSED"]
orders[3] = "COMPLETE"
orders.append(500)
orders.insert(3,250)
print(orders)
#print(type(orders))
#print(orders)

#tuple
orders_tuple = (1, "2013-07-25 00:00:00.0", 11599, "CLOSED")
#orders_tuple.append(200)    #AttributeError: 'tuple' object has no attribute 'append'
print(orders_tuple)
#print(type(orders_tuple))
#orders_tuple[3] = "COMPLETE"   #TypeError: 'tuple' object does not support item assignment
#print(orders_tuple)

#integer type value
order = [5, 4, 6, 7, 3]
print(order)
print(min(order))
print(max(order))

#sting type value
orders = ['sunny', 'lokki', 'bindhu', 'uncle', 'aunty', 'gnanesh']
print(orders)
print(min(orders))
print(max(orders))
#Finding the minimum and maximum in a mixed-type list (e.g., integers and strings) will raise an error.

print(orders.pop())
print(orders)

for x in orders:
    print(orders)

#Summing Numbers from 1 to 10
range_start = int(input('Enter the starting range: '))
range_end = int(input('Enter the endinge range: '))
numbers = range(range_start, range_end+1)
total_sum = 0
for x in numbers:
    total_sum += x
    #print(total_sum)
    print(f"sum of the numbers from {range_start} to {range_end} is {total_sum}")

# using for loop, correctly sum only the valid numeric values, ignoring any `None` or invalid entries.
order_amounts = [100, 200, None, 'invalid', 400, 350.50]
sum = 0
for x in order_amounts:
    if isinstance(x, (int, float)):
        sum += x
    else:
        continue
print(f"the sum of order value amount is {sum}.")

#We can achieve the same result with a `while` loop. Here's how:
order_amounts = [100, 200, None, "invalid", 300, 400.5]
#print(len(order_amounts))
sum = 0
i = 0
while i < len(order_amounts):
    if isinstance(order_amounts[i], (int, float)):
        sum += order_amounts[i]
    i += 1
print(f"The sum of valid order amounts is {sum}.")

#Alternatively, you can use a `while True` loop with a `break` condition:
order_amounts = [100, 200, None, "invalid", 300, 400.5]
sum = 0
i = 0
while True:
    if isinstance(order_amounts[i], (int, float)):
        sum += order_amounts[i]
    i += 1
    if i == len(order_amounts):
        break
print(f"The sum of valid order amounts is {sum}.")

#Finding the Index of an Element:
orders = [11599, 11588, 11599, 11577]
index = orders.index(11577)
print(f"Order ID 11599 is found at index {index}.")
#If the element is not found, the program will throw an error.
print(11599 in orders)  # Returns True
print(12345 in orders)  # Returns False
#This method doesn't return the index but tells us if the element is present.

#Counting Occurrences:
orders = [50, 40, 50, 30, 50]
count_50 = orders.count(50)
print(f"Order ID 50 appears {count_50} times.")
#Sorting and Reversing:
orders.sort()  # Sorts in ascending order
print(orders)
orders.reverse()  # Reverses the list
print(orders)

#Unique Elements:
customer_ids = [102, 105, 102, 103, 107, 109, 110, 109]
unique_customers = []
for x in customer_ids:
    if x not in unique_customers:
        unique_customers.append(x)
print(unique_customers)
'''
#Alternatively, using a set:
customer_ids = [102, 105, 102, 103, 107, 109, 110, 109]
unique_customers = list(set(customer_ids))
print(unique_customers)
#Sets automatically handle duplicates, making this method more efficient.




