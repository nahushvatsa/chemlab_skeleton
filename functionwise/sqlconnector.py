import mysql.connector
mydb = mysql.connector.connect(      #String values given here are assuming the user is connecting to a local SQL server. 
  host="localhost",                  #Ergo, values may change user by user depending on their SQL server.
  user="root",
  password="[your password]",        #String value for password is acting as a placeholder here. Use your MySQL's password. 
  database="chemlab"
)

mycursor = mydb.cursor()
