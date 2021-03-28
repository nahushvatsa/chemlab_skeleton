import mysql.connector
mydb = mysql.connector.connect(
  host="localhost3306",
  user="root",
  password="tiger",
  database="chemlab"
)

mycursor = mydb.cursor()
