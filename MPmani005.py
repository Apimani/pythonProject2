import sqlite3
#print(sqlite3.version)

# Step 1: Connect to SQLite (in-memory database)
connection = sqlite3.connect(':memory:')  # Use ':memory:' for an in-memory DB
# Or use a file-based DB: sqlite3.connect('example.db')

# Step 2: Create a Cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Execute SQL queries
# Create a table
cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT
    )
''')

# Insert data into the table
cursor.executemany('''
    INSERT INTO employees (name, age, department)
    VALUES (?, ?, ?)
''', [
    ('Alice', 30, 'HR'),
    ('Bob', 25, 'Engineering'),
    ('Charlie', 28, 'Sales')
])

# Fetch data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

# Print results
print("Employees Table:")
for row in rows:
    print(row)

# Step 4: Close the connection
connection.close()


