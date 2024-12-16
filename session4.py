print("Hi Pitchaimani Mani, Good Morning. Have a nice day!")
'''
order_amounts = [100, 200, 500, 1500, 2000, 3000, 4500, 5500]
orders_including_gst = []
for x in order_amounts:
    orders_including_gst.append(x + x * 0.18)
print(orders_including_gst)

#Example with Varying GST Rates
order_amounts_with_gst = [(100, 5), (200, 18), (500, 12), (1500, 18), (2000, 5), (3000, 28), (4500, 12), (5500, 18)]
orders_including_gst = [amount + (amount * gst / 100) for amount, gst in order_amounts_with_gst]
print(orders_including_gst)

#Creating a Nested List:
nested_list = [[i, i**2, i**3] for i in range(1, 11)]
print(nested_list)
#Flattening the Nested List:
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

#Filtering Orders by Status
orders_list = [
    [1, '2024-08-01', 'C123', 'Closed'],
    [2, '2024-08-02', 'C124', 'Pending'],
    [3, '2024-08-03', 'C125', 'Closed'],
    [4, '2024-08-04', 'C126', 'Shipped']
]
x = int(input('enter the position of index: '))
y = (input('enter the searching value: '))
closed_orders = [order for order in orders_list if order[x] == y]
print(closed_orders)

input_list = ["hello", "hello", "I", "am", "Sumit", "Sumit"]
result_list = []
for word in set(input_list):
    result_list.append((word, input_list.count(word)))
    print(result_list)
input_list_lower = [word.lower() for word in input_list]
print(input_list_lower)
'''
#take input from the user
input_text = input("Enter the text: ")
input_list = input_text.split()
result_list = []
for word in set(input_list):
    result_list.append((word, input_list.count(word)))
    print(result_list)