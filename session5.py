
print("Hi Pitchaimani Mani, Good Morning. Have a nice day!")
'''
word_dictionary = {
    'intelligent': 'the one who is really brilliant',
    'rich': 'a person who has a lot of money',
    'car': 'a four-wheeler vehicle'
}
print(word_dictionary)
print(word_dictionary['intelligent'])

#Python will raise a `KeyError`. To avoid this, use the `get()` method, which returns `None` if the key is not found:
print(word_dictionary.get('bike'))

#Adding and Modifying Entries
word_dictionary['bike'] = 'a two-wheeler vehicle'
word_dictionary['car'] = 'a four-wheel vehicle'
print(word_dictionary)

#get all the keys or values in a dictionary using the `keys()` and `values()` methods:
print(word_dictionary.keys())
print(word_dictionary.values())

# Dictionary Operations
#Length of a dictionary
print(len(word_dictionary))

#Clearing a dictionary
word_dictionary.clear()
print(word_dictionary)


# Real-Time Use Case
#Suppose you have the following list of tuples representing orders:
orders_data = [
    (101, 10000),
    (102, 20000),
    (103, 15000)
]
print(orders_data)

#We can convert this list of tuples into a dictionary
orders_dict = dict(orders_data)
print(orders_dict)
print(orders_dict.keys())
print(orders_dict.values())
print(orders_dict[101])
'''

customers_raw_data = """customer_id, customer_fname, customer_ln
11599, Mary, Malone, 8708 Indian Horse Highway, Hickory, NC, 28601
256, David, Rodriguez, 7605 Tawny Horse Falls, Chicago, IL, 60625
12111, Amber, Franco, 8766 Clear Prairie Line, Santa Cruz, CA, 95060
8827, Brian, Wilson, 8396 High Corners, San Antonio, TX, 78240
11318, Mary, Henry, 3047 Silent Embers Maze, Caguas, PR, 00725"""  #multi-line string
print(customers_raw_data)

#first line is not data but rather a header, so let me separate it out.
customer_header = customers_raw_data.split("\n")[0]
print(customer_header)

#separate out the data:
customer_data = customers_raw_data.split("\n")[1:]
print(customer_data)

#let's create a dictionary:
customer_dictionary = {}

#add it to `customer_dictionary`
for x in customer_data:
    customer_dictionary[x.split(",")[0]] = tuple(x.split(",")[1:])
    print(customer_dictionary)

#retrieve all details for a specific customer:
    print(customer_dictionary["11599"])

#how we can simplify this using dictionary comprehension:
#customer_dictionary = {x.split(",")[0]: tuple(x.split(",")[1:]) for x in customer_data}
#print(customer_dictionary)

#to create a nested dictionary
nested_dictionary = {}
for key, value in customer_dictionary.items():
    nested_dictionary[key] = {
        "First Name": value[0],
        "Last Name": value[1],
        "Address": value[2],
        "City": value[3],
        "State": value[4],
        "Pincode": value[5]
    }
    print(nested_dictionary)
    print(nested_dictionary["11599"]["Pincode"])

    header_list = customer_header.split(",")
    nested_dictionary = {}
    for key, value in customer_dictionary.items():
        nested_dictionary[key] = {header_list[i]: value[i] for i in range(len(header_list))}
    print(nested_dictionary)
