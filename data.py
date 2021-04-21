
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="you",database="smndubot")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS messages")

sql = """CREATE TABLE `messages` (
	`sender_id` INT NOT NULL,
	`sender_name` TEXT,
	`sender_username` TEXT,
	`message_id` INT NOT NULL,
	`chat_id` INT NOT NULL,
	`text` LONGTEXT,
	`attachments` TINYINT DEFAULT '0',
	`attachments_id` TEXT DEFAULT NULL,
	`time` TIMESTAMP default CURRENT_TIMESTAMP
);"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

















