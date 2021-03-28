from newuser import *
from validator import *
from login import *
from mainmenu import *
import sys

def acctMenu():
  print('''Welcome to the Chemistry Lab Manager. Please Login or Sign up to continue!
  Please enter one of the following numbers as an option to continue

  1 - Login
  2 - Sign Up
  3 - Exit Program 
  ''')

  optMain = inputvalidator('Enter Option - ', (1,2,3))

  if optMain == 1:
    login()
  elif optMain == 2:
    createuser()
  elif optMain == 3:
    print('Thank you for using our program! We hope to see you again!')
    sys.exit()
