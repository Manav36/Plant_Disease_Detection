import MySQLdb

# Database connection details
host = 'localhost'
user = 'root'
password = ''
database = 'user-system'

try:
    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", user="root", password="", db="user-system")
    cursor = conn.cursor()
    print("Connected to the database successfully.")

    # Test querying the table
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

except MySQLdb.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.open:
        conn.close()
