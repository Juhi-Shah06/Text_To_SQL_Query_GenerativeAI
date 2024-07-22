import sqlite3


# Connet to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

#insert records
cursor.execute('''Insert into STUDENT values('Juhi','AI/ML','A',95)''')
cursor.execute('''Insert into STUDENT values('Akshat','React.js','A',100)''')
cursor.execute('''Insert into STUDENT values('Ishika','AI/ML','B',94)''')
cursor.execute('''Insert into STUDENT values('Aniket','DevOps','B',93)''')
cursor.execute('''Insert into STUDENT values('Rohit','Python','C',91)''')
cursor.execute('''Insert into STUDENT values('Komal','DevOps','C',92
               )''')

# Display all the records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
