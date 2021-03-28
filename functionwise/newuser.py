from validator import *
from mysqlconnector import *
from encrypt import *
from mainmenu import *

def createuser():
  name = inputvalidator('Enter name: ')
  email = inputvalidator('Enter email: ','email')
  print('Your Password should have atleast 6 characters, a number, and an uppercase character. Please note that your password is encrypted and safe in our database :)')
  passw = inputvalidator('Create a password - ','password')
  print('Account Created Successfully!')
  
  passw = encrypt(passw)
  
  statement = "INSERT INTO `chemlab`.`accounts`(`Name`,`Email`,`Password`,`Accounttype`,`Datejoined`) VALUES('"+name+"','"+email+"','"+passw+"','student',curdate())"

  mycursor.execute(statement)
  mydb.commit()

  mainmenu(email)

