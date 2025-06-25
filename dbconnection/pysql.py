import pymysql

# Connect to DB
connection =pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="billing",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Create Table
        # create_query ="""
        # CREATE TABLE IF NOT EXISTS employees (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100),
        #     department VARCHAR(100)
        #     );
        # """
        # cursor.execute(create_query)
        #
        # # Insert query
        # insert_query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        # values = [("John", "IT"), ("Alice", "HR"), ("Bob", "Finance")]
        # cursor. executemany(insert_query, values)
        # connection. commit()

        # Select Data
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()
        # print(result)

        with open("employee.txt","w") as f:
            for row in result:
                f.write(f"{row}\n")

finally:
    connection.close()