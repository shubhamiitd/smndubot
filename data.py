
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="you",database="smndubot")

cursor = db.cursor()

# Create table as per requirement
sql = """CREATE TABLE `users` (
	`username` TEXT DEFAULT NULL,
	`user_id` INT,
	`is_admin` TINYINT DEFAULT '0',
	`last_access` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


















