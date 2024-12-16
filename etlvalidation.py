import pandas as pd

# Read the CSV file
source = pd.read_csv("Employee.csv", sep=",", engine='python')

# Test Case 1: Display column names
print("Test Case 1: Following are the column names in the source file:\n")
print(source.columns)
print("\n")

# Test Case 2: Display the shape (rows x columns)
print("Test Case 2: Rows x columns in the source file:\n")
print(source.shape)
print("\n")

# Test Case 3: Display the number of non-NA/null entries for each column
print("Test Case 3: No. of rows under each column:\n")
print(source.count())
print("\n")

# Test Case 4: Count duplicate records
print("Test Case 4: Duplicate records in the source:\n")
print(source.duplicated().sum())
print("\n")

# Test Case 5: Save duplicate records to a new file
print("Test Case 5: Duplicate records saved in the file 'duplicated.csv':\n")
dupes = source[source.duplicated()]
dupes.to_csv("duplicated.csv", index=False)
print("\n")

# Test Case 6: Check for NULL values in the 'department' column
print("Test Case 6: Check if NULL values exist in the 'department' column:\n")
print(source[source['department'].isnull()])
print("\n")

# Test Case 6_a: Check for NULL values in the 'salary' column
print("Test Case 6_a: Check if NULL values exist in the 'salary' column:\n")
print(source[source['salary'].isnull()])
print("\n")

# Test Case 7: Unique values in the 'email' column
print("Test Case 7: Unique values in the 'email' column:\n")
print(source['email'].unique())
print("\n")

# Test Case 8: Unique values in the 'emp_name' column
print("Test Case 8: Unique values in the 'first_name' column:\n")
print(source['first_name'].unique())
print("\n")

# Test Case 9: Unique values in the 'department' column
print("Test Case 9: Unique values in the 'department' column:\n")
print(source['department'].unique())
print("\n")

# Test Case 10: Unique values in the 'salary' column
print("Test Case 10: Unique values in the 'salary' column:\n")
print(source['salary'].unique())
print("\n")

# Test Case 11: Display the first 5 rows of the dataset
print("Test Case 11: Sample (top 5) records from the source file:\n")
print(source.head())
print("\n")

# Test Case 12: Display the last 5 rows of the dataset
print("Test Case 12: Sample (bottom 5) records from the source file:\n")
print(source.tail())
print("\n")

print("TEST COMPLETED....\n")
