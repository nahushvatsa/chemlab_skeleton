from mysqlconnector import *
from validator import *
from saltanalysis import *
from acctmenu import *
import sys
from encrypt import *

def mainmenu(email):
  statement = 'SELECT Name FROM accounts WHERE Email = \'' + email + '\''
  mycursor.execute(statement)
  name = mycursor.fetchall()
  name = name[0][0]
  print('Welcome Back', name + '!')
  
  statement = "SELECT Accounttype FROM accounts WHERE Email = '"+email+"'"
  mycursor.execute(statement)
  accounttype = mycursor.fetchall()
  accounttype = accounttype[0][0]
  if accounttype == 'student':
    mainstudent(email)
  else:
    mainadmin(email)

def mainstudent(email):
  print('''
  1) Rent Equipment
  2) Return Equipment
  3) Check Balance
  4) Run Salt Analysis
  5) Check Currently Rented Equiment
  6) Change Password
  7) Check Availible Items 
  8) Log out
  9) Exit \n''')
  
  choice = inputvalidator('Enter a option - ',(1,2,3,4,5,6,7,8,9))
  print()
  perm = 'student'
  
  if choice == 1:
    rent(email)
  elif choice == 2:
    returnequipment(email)
    mainstudent(email)
  elif choice == 3:
    print('Your current balance is -', bal(email), 'Dhs')
    mainstudent(email)
  elif choice == 4:
    saltanalysis()
    mainstudent(email)
  elif choice == 5:
    current(email)
    mainstudent(email)
  elif choice == 6:
    changepassword(email)
    mainstudent(email)
  elif choice==7:
    availcheck()
    mainstudent(email)
  elif choice == 8:
    print('You have successfully logged out. You will now be redirected to the homepage!')
    acctMenu()
  elif choice == 9:
    print('Thank you for using our ChemLab Manager! We hope to see you again!')
    sys.exit()

def mainadmin(email):
  print('''
  1) Check Available items
  2) Rent Equiment
  3) Return Equipment
  4) Check Balance of any User
  5) Check Currently Rented Equipment of any User
  6) Run Salt Analysis
  7) Change Password
  8) Log out
  9) Exit''')

  opt = inputvalidator('Enter option - ', (1,2,3,4,5,6,7,8,9))
  perm = 'admin'
  
  if opt == 2:
    rent(email)
  elif opt == 3:
    returnequipment(email)
    mainadmin(email)
  elif opt == 4:
    while True: 
      mail_ch = inputvalidator('Enter User\'s Email - ', 'email')
      state = 'SELECT Email FROM accounts'
      mycursor.execute(state)
      data = mycursor.fetchall()
      lis = []
      for i in range(len(data)):
        lis.append(data[i][0])
      if mail_ch in lis:
        print('The User\'s Balance is - ', bal(mail_ch), 'Dhs')
        break
      else:
        print('This Email does not exist! Please try again!')
        continue
    mainadmin(email)
  elif opt == 6:
    saltanalysis()
    mainadmin(email)
  elif opt == 5:
    while True: 
      mail_ch = inputvalidator('Enter User\'s Email - ', 'email')
      state = 'SELECT Email FROM accounts'
      mycursor.execute(state)
      data = mycursor.fetchall()
      lis = []
      for i in range(len(data)):
        lis.append(data[i][0])
      if mail_ch in lis:
        current(mail_ch)
        break
      else:
        print('This Email does not exist! Please try again!')
        continue
    mainadmin(email)
  elif opt == 7:
    changepassword(email)
    mainadmin(email)
  elif opt == 1:
    availcheck()
    mainadmin(email)
  elif opt == 8:
    print('You have successfully logged out. You will now be redirected to the homepage!')
    acctMenu()
  elif opt == 9:
    print('Thank you for using our ChemLab Manager! We hope to see you again!')
    sys.exit()
    
def bal(email):
  
  statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\'' 
  mycursor.execute(statement)
  bal = mycursor.fetchall()
  bal = bal[0][0]

  statement1="UPDATE rentedequipment SET datetime2=NOW()"
  mycursor.execute(statement1)
  mydb.commit()
  main = 'SELECT rentedequipment.email, rentedequipment.equipment, rentedequipment.quantity, totalequipment.Price, (time_to_sec(timediff(rentedequipment.datetime2, rentedequipment.datetime))/3600) FROM rentedequipment, totalequipment WHERE (rentedequipment.equipment = totalequipment.EquipmentName) AND rentedequipment.email = "' + email + '"'

  hours = 0
  minutes = 0
  expd = 0

  mycursor.execute(main)
  data = mycursor.fetchall()

  for i in range(len(data)):
    tim = data[i][4]*60

    if tim > 60:
      hours = tim//60
      minutes = int(tim % 60)
    if minutes >= 30:
      hours += 1

    expd += data[i][3]*hours + data[i][2]

  bal = bal - expd
  return bal

def rent(email):
  statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\'' 
  mycursor.execute(statement)
  bal = mycursor.fetchall()
  bal = bal[0][0]
  if bal>0:
    EquipmentName = (inputvalidator('What equipment would you like to rent - ')).lower()
    statement = "SELECT Price,AvailibleStock FROM totalequipment WHERE EquipmentName = '"+EquipmentName+"'"
    mycursor.execute(statement)
    result = mycursor.fetchall()
    if result == []:
      print(EquipmentName, 'is not a valid Item!')
    else:
      price = result[0][0]
      stock = result[0][1]
      quantity=inputvalidator('Enter Quantity to rent - ','int')
      if quantity > result[0][1]:
        print('We have only',result[0][1],'of'+ EquipmentName + 's in stock, Please try again later')
      else:
        res = stock - quantity
        statement1 = 'UPDATE totalequipment SET AvailibleStock = ' + str(res) + ' WHERE EquipmentName = "' + EquipmentName + '"'
        statement2 = "INSERT INTO rentedequipment VALUES('{}' , '{}' , '{}' , NOW(), NOW())".format(email,EquipmentName,str(quantity))
        
        mycursor.execute(statement1)
        mycursor.execute(statement2)
        mydb.commit()
        print("You have successfully rented", quantity, EquipmentName + '(s)')
  else:
    print("You do not have enough balance to rent an item!")
  mainstudent(email)

def returnequipment(email):
  statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\'' 
  mycursor.execute(statement)
  bal = mycursor.fetchall()
  bal = bal[0][0]
  statement1="UPDATE rentedequipment SET datetime2=NOW()"
  statement2="SELECT rentedequipment.equipment, rentedequipment.quantity, (time_to_sec(timediff(rentedequipment.datetime2, rentedequipment.datetime))/3600), totalequipment.Price  FROM rentedequipment, totalequipment WHERE (rentedequipment.equipment = totalequipment.EquipmentName) AND email='{}'".format(email)
  mycursor.execute(statement1)
  mydb.commit()
  mycursor.execute(statement2)
  data = mycursor.fetchall()
  if data == []:
    print('You have no items to return!')
  else:
    print("Select item to return:")
    for i in range(len(data)):
      print('***** ITEM ' + str(i + 1) + ' *****')
      print(data[i][1],data[i][0]+'(s)')
    option = inputvalidator('Enter choice : ',tuple(range(1, len(data)+1)))
    expd = 0
    minutes = 0
    hours = 0
    for i in range(len(data)):
      if data[i][0] == data[option-1][0]:
        tim = data[i][2]*60

        if tim > 60:
          hours = tim//60
          minutes = int(tim % 60)
        if minutes >= 30:
          hours += 1

        expd += data[i][3]*hours + data[i][1]

    bal = bal - expd
    statement1="UPDATE accounts SET Balance={} WHERE email='{}'".format(bal,email)
    statement2="DELETE from rentedequipment WHERE (email='{}' AND equipment='{}' AND quantity={})".format(email,data[option-1]
    [0],data[option-1][1])
    statement3="UPDATE totalequipment SET AvailibleStock=AvailibleStock+{} WHERE EquipmentName = '{}'".format(data[option-1][1],data[option-1][0])
    mycursor.execute(statement1)
    mycursor.execute(statement2)
    mycursor.execute(statement3)
    
    mydb.commit()
    
    print('Item returned successfully!')
  

def current(email):
  statement1="UPDATE rentedequipment SET datetime2=NOW()"
  statement2="SELECT equipment, quantity, (time_to_sec(timediff(datetime2, datetime))/3600) FROM rentedequipment WHERE email='{}'".format(email)
  mycursor.execute(statement1)
  mydb.commit()
  mycursor.execute(statement2)
  data = mycursor.fetchall()
  if data == []:
    print('No items currently rented')
  else:
    for i in range(len(data)):
      print('***** ITEM ' + str(i + 1) + ' *****')
      print('Equipment Name - ', data[i][0])
      print('Quantity rented - ', data[i][1])
      hours = 0
      minutes = 0
      tim = data[i][2] * 60
      if tim > 60:
        hours = tim // 60
        minutes = tim % 60
        print('Time rented - ', hours, 'Hour(s) and', int(minutes), 'Minutes')
      else:
        print('Time rented - ', int(tim), 'Minutes')

def availcheck():
  print('Below is a list of all items we offer!')
  print()
  print("Item - Availible Stock - Price")
  print()
  statement = "SELECT EquipmentName, AvailibleStock, Price from totalequipment"
  mycursor.execute(statement)
  data = mycursor.fetchall()
  for x in data:
    print(x[0],'-',x[1],'in stock!','-','AED',x[2])

def changepassword(email):
  passw = inputvalidator('Create a new password! - ','password')
  passw=encrypt(passw)
  statement = "UPDATE accounts set Password = '{}' WHERE email = '{}'".format(passw,email)
  mycursor.execute(statement)
  mydb.commit()
  print('Password changed successfully! You will now be redirected to the homepage!\n')

  
