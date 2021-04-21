
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="you",database="smndubot")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS users")

sql = """CREATE TABLE `users` (
	`firstname` TEXT DEFAULT NULL,
	`username` TEXT DEFAULT NULL,
	`user_id` INT,
	`is_admin` TINYINT DEFAULT '0',
	`last_access` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);"""

cursor.execute(sql)
sql = """INSERT INTO users(firstname, username,
         user_id, is_admin)
         VALUES ('Shubham','sy_tele', 793347625, 1 )"""

  
# loop through the rows
for row in result:
    print(row)
    print("\n")
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# execute your query
cursor.execute("SELECT * FROM users")
  
# fetch all the matching rows 
result = cursor.fetchall()
















