from validator import *
from encrypt import *
from mysqlconnector import *
from newuser import *
from mainmenu import *
import sys

def login():
  print('Welcome! Please Log In to get started!')

  mail_opt = inputvalidator('Enter Email - ','email')
  mycursor.execute('SELECT Email FROM accounts')
  records = mycursor.fetchall()
  check = (mail_opt,)
  n = 0
  if check in records:
    pass_opt = inputvalidator('Enter Password - ')
    pass_opt = encrypt(pass_opt)
    statement = 'SELECT Password FROM accounts WHERE Email = \'' + mail_opt + '\''
    mycursor.execute(statement)
    verify = mycursor.fetchall()
    correctpass = verify[0][0]
    while True:
      if pass_opt != correctpass: 
        n += 1
        print('Invalid Password! Please try again!')
        if n != 3:
          pass_opt = inputvalidator('Enter Password - ')
          pass_opt = encrypt(pass_opt)
          continue
        else:
          print('You have entered a wrong password 3 times. You will now be logged out and the program will close!')
          sys.exit()
      else:
        mainmenu(mail_opt)
        break

  else:
    choice = inputvalidator('You do not have an account with us, Would you like to create one? - ','yesno')
    if choice:
      createuser()
    else:
      sys.exit()
