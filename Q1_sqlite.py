import sqlite3

# Connect to the database.
# If the database file does not exist, SQLite creates it.
connection = sqlite3.connect("assignment2.db")

# Create a cursor to execute SQL commands.
cursor = connection.cursor()

# Create a table.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    mark INTEGER
)
""")

# Insert sample data.
cursor.execute(
    "INSERT INTO students (name, mark) VALUES (?, ?)",
    ("Alice", 75)
)

cursor.execute(
    "INSERT INTO students (name, mark) VALUES (?, ?)",
    ("Brian", 82)
)

cursor.execute(
    "INSERT INTO students (name, mark) VALUES (?, ?)",
    ("Diana", 91)
)

# Save the changes.
connection.commit()

# Retrieve the data.
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students in the database:")
for row in rows:
    print(row)

# Close the connection.
connection.close()