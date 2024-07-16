import sqlite3

# Connect to the database
connection = sqlite3.connect('student.db')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create the table Student with name(varchar 25), class(varchar 25), section(varchar 25), name(int)
table_info = """
CREATE TABLE Student(
name VARCHAR(25),
class VARCHAR(25),
section VARCHAR(25),
marks INT
);
"""
cursor.execute(table_info)

# Define a function to insert records into Student table
def insert_record(name, class_name, section, marks):
    cursor.execute("INSERT INTO Student VALUES (?, ?, ?, ?)", (name, class_name, section, marks))
    connection.commit()

# Insert 10 records into Student table
insert_record('John', '10', 'A', 85)
insert_record('Jane', '10', 'B', 92)
insert_record('Mark', '11', 'A', 78)
insert_record('Emily', '11', 'B', 95)
insert_record('David', '12', 'A', 90)
insert_record('Sarah', '12', 'B', 88)
insert_record('Michael', '10', 'A', 92)
insert_record('Jessica', '11', 'B', 85)
insert_record('Robert', '12', 'A', 78)
insert_record('Emma', '10', 'B', 95)
insert_record('Daniel', '11', 'A', 88)

# Create a function to display all the records of the Student table
def display_records():
    cursor.execute("SELECT * FROM Student")
    records = cursor.fetchall()
    for record in records:
        print(record)

print("The inserted records are:")
display_records()

# Create a Function to commit and close the connection
connection.commit()
connection.close()