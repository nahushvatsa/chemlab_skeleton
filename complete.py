import sys
import mysql.connector


def acctMenu():
    print(
        '''Welcome to the Chemistry Lab Manager. Please Login or Sign up to continue!
  Please enter one of the following numbers as an option to continue

  1 - Login
  2 - Sign Up
  3 - Exit Program 
  ''')

    optMain = inputvalidator('Enter Option - ', (1, 2, 3))

    if optMain == 1:
        login()
    elif optMain == 2:
        createuser()
    elif optMain == 3:
        print('Thank you for using our program! We hope to see you again!')
        sys.exit()


def encrypt(text):
    text = text[::-1]
    s = 4
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def login():
    print('Welcome! Please Log In to get started!')

    mail_opt = inputvalidator('Enter Email - ', 'email')
    mycursor.execute('SELECT Email FROM accounts')
    records = mycursor.fetchall()
    check = (mail_opt, )
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
                    print(
                        'You have entered a wrong password 3 times. You will now be logged out and the program will close!'
                    )
                    sys.exit()
            else:
                mainmenu(mail_opt)
                break

    else:
        choice = inputvalidator(
            'You do not have an account with us, Would you like to create one? - ',
            'yesno')
        if choice:
            createuser()
        else:
            sys.exit()


def createuser():
    name = inputvalidator('Enter name: ')
    email = inputvalidator('Enter email: ', 'email')
    print(
        'Your Password should have atleast 6 characters, a number, and an uppercase character. Please note that your password is encrypted and safe in our database :)'
    )
    passw = inputvalidator('Create a password - ', 'password')
    print('Account Created Successfully!')

    passw = encrypt(passw)

    statement = "INSERT INTO `chemlab`.`accounts`(`Name`,`Email`,`Password`,`Accounttype`,`Datejoined`) VALUES('" + name + "','" + email + "','" + passw + "','student',curdate())"

    mycursor.execute(statement)
    mydb.commit()

    mainmenu(email)


def saltanalysis():
    # Salt Analysis Program
    # Defining systemaic anion tests
    def invalid():
        while True:
            print("We do not have this salt")

    def Carbonatesystematic():
        value = int(
            input("""Add some dilute HCL to your salt,
  Press 1 if you observe Brisk Effervesence
  Press 2 if you do not observe Brisk Effervesence - """))
        if value == 1:
            return "Carbonate"
        else:
            return False

    def Acetatesystematic():
        value = int(
            input(
                """Rub your salt with dilute H2SO4 with the help of a glass rod,
  Press 1 if the vinegar smell intensifies
  Press 2 if the vinegar snell does not intensify - """))
        if value == 1:
            return "Acetate"
        else:
            return False

    def clno3systematic():
        value = int(
            input("""Treat your salt with some concentrated H2SO4,
  Press 1 if you observe Pungent smelling white fumes
  Press 2 if you observe a brown gas
  Press 3 if you do not observe any of the above - """))
        if value == 1:
            return "Chloride"
        elif value == 2:
            return "Nitrate"
        else:
            return False

    def Sulphatesystematic():
        value = int(
            input("""Treat your salt with some BaCl2,
  Press 1 if you observe a white precipitate
  Press 2 if you do not observer a white precipitate - """))
        if value == 1:
            return "Sulphate"
        else:
            return False

    # Systematic anion tests done
    # Defining systematic cation tests
    def Ammoniumsystematic():
        value = int(
            input("""Prepare a salt solution and then add some Na2CO3 to it,
  Press 1 if you DO NOT observe a precipitate
  Press 2 if none of the above - """))
        if value == 1:
            return "Ammonium"
        else:
            return False

    def Group5aluminumsystematic():
        value = int(
            input("""Prepare a dilute solution of your salt,
  Then add some dilute HCl to it,
  Press 1 if you observe White Precipitate
  Press 2 if none of the above - """))
        if value == 1:
            return "Lead"
        else:
            value1 = int(
                input(
                    """Continue by adding a pinch of NH4Cl to the same solution,Shake well,
  Add some NH4OH to the mixture aswell
  Press 1 if you observe a white gelatinous ppt
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Aluminum"
            else:
                value2 = int(
                    input(
                        """Continue by adding some Ammonium Carbonate to your mixture,
  Press 1 if you observe a white ppt
  Press 2 if you do not observe a white ppt - """))
                if value2 == 1:
                    return "Group5"
                else:
                    return False

    # Systematic tests for cation done
    # Confirmatory tests for cation
    def Leadconfirmatory():
        value = int(
            input(
                """Boil some of your salt with water,then add some K2CrO4 to it,
  Press 1 if you observe a yellow ppt
  Press 2 if you do not observe a yellow ppt - """))
        if value == 1:
            return "Lead"
        else:
            return False

    def Group5flame():
        value = int(
            input("""Add some of your salt to a watchglass,
  Add some concetrated HCl to it,
  Rub with a glass rod,
  Hold the glass rod to the flame,
  Press 1 if you observe a Pale green flame
  Press 2 if you observe a Crimson red flame
  Press 3 if you observe a Brick red flame - """))
        if value == 1:
            return "Barium"
        elif value == 2:
            return "Strontium"
        else:
            return "Calcium"

    def Bariumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some pottassium chromate to your salt,
  Press 1 if you observe a Yellow ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Barium"
        else:
            return False

    def Strontiumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some ammonium sulphate to your salt,
  Press 1 if you observe a white ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Strontium"
        else:
            return False

    def Calciumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some Ammonium Oxalate to your salt,
  Press 1 if you observe a white ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Calcium"
        else:
            return False

    def Ammoniumconfirmatory():
        value = int(
            input("""Add few drops of Nessler's reagent to your salt,
  Press 1 if you observe Reddish Brown color
  Press 2 if none of the above - """))
        if value == 1:
            return "Ammonium"

    def Aluminumconfirmatory():
        value = int(
            input(
                """Dip a strip of filter paper in a cobalt nitrate-dilute HNO3 solution of your salt,
  Hold the strip to a flame
  Burn the ash
  Press 1 if you observe blue tinted ash
  Press 2 if none of the above - """))
        if value == 1:
            return "Aluminum"
        else:
            return False

    # Confirmatory tests for cation done
    # Confirmatory tests for anions
    def Acetateconfirmatory():
        value = int(
            input("""Add a few drops of neutral Ferric chloride to your salt,
  Press 1 if you observe a Reddish Brown coloration
  Press 2 if none of th above - """))
        if value == 1:
            return "Acetate"
        else:
            return False

    def Carbonateconfirmatory():
        value = int(
            input("""Add some BaCl2 to your solution,
  Press 1 if you observe a white precipitate
  Press 2 if none of the above - """))
        if value == 1:
            value1 = int(
                input("""Continue by adding some HCl to your mixture,
  Press 1 if you observe Brisk Effervesence
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Carbonate"
            else:
                return False
        else:
            return False

    def Chlorideconfirmatory():
        value = int(
            input("""Prepare a dilute HNO3 solution of your salt,
  Add a few drops of AgNO3 to it,
  Press 1 if you observe a White ppt
  Press 2 if none of the above - """))
        if value == 1:
            value1 = int(
                input("""Continue by adding excess of NH4OH to your mixture,
  Press 1 if your white ppt dissolves
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Chloride"
            else:
                return False
        else:
            return False

    def Sulphateconfirmatory():
        value = int(
            input("""Add some Acetic acid to your salt solution,
  Add some Lead acetate to your mixture,
  Press 1 if you observe a white ppt
  Press 2 if none of the above - """))
        if value == 1:
            return "Sulphate"
        else:
            return False

    def Nitrateconfirmatory():
        value = int(
            input("""Add few drops of Diphenylamine to your salt,
  Press 1 if you observe Deep blue coloration
  Press 2 if none of the above - """))
        if value == 1:
            return "Nitrate"
        else:
            return False

    probableanions = []
    probablecations = []
    notprobableanions = []
    notprobablecations = []
    anionsystematic = ["Carbonate", "Acetate", "clno3", "Sulphate"]
    cationsystematic = ["Ammonium", "Group5aluminum"]
    anionconfirmatory = [
        "Acetate", "Carbonate", "Chloride", "Sulphate", "Nitrate"
    ]
    cationconfirmatory = [
        "Ammonium", "Lead", "Barium", "Strontium", "Calcium", "Aluminum"
    ]
    # Prelimnary Tests
    # Odour Prelimnary
    while True:
        odour = int(
            input("""Enter the odour of the salt if any:
    Press 1 for Ammoniacal odour
    Press 2 for Vinegar odour
    Press 3 for no significant odour - """))
        if odour == 1:
            probablecations.append("Ammonium")
            break
        elif odour == 2:
            probableanions.append("Acetate")
            break
        elif odour == 3:
            notprobableanions.append("Acetate")
            notprobablecations.append("Ammonium")
            break
        else:
            print("Invalid choice, Enter again")
    # Solubility in Water prelimnary
    while True:
        watersoluble = int(
            input("""Is your salt soluble in water?
  Press 1 for yes
  Press 2 for no - """))
        if watersoluble == 1:
            if "Ammonium" not in probablecations:
                probablecations.append("Ammonium")
                if "Ammonium" in notprobablecations:
                    notprobablecations.remove("Ammonium")
            break
        elif watersoluble == 2:
            break
        else:
            print("Invalid choice, Enter again")
    # Solubility in dil HCL Prelimnary
    while True:
        dilhclsoluble = int(
            input("""Is your salt soluble in dilute HCL?
  Press 1 for yes
  Press 2 for no - """))
        if dilhclsoluble == 1:
            if "Lead" not in notprobablecations:
                notprobablecations.append("Lead")
                break
            break
        elif dilhclsoluble == 2:
            break
        else:
            print("Invalid choice, Enter again")
    # Prelimnary tests done
    # Systematic tests anion
    otheranions = []
    for x in anionsystematic:
        if x not in probableanions and x not in notprobableanions:
            otheranions.append(x)
    finalsystematicanion = probableanions + otheranions + notprobableanions
    for x in finalsystematicanion:
        anion = eval(x + "systematic" + "()")
        if anion:
            # Confirmatory tests anion
            conanion = eval(anion + "confirmatory" + "()")
            if conanion:
                break
    # ANION DONE
    # Systematic tests cation
    othercations = []
    for x in cationsystematic:
        if x not in probablecations and x not in notprobablecations:
            othercations.append(x)
    finalsystematiccation = probablecations + othercations + notprobablecations
    for x in finalsystematiccation:
        cation = eval(x + "systematic" + "()")
        if cation == "Group5":
            cation = Group5flame()
        if cation:
            # Confirmatory for cation
            concation = eval(cation + "confirmatory" + "()")
            if concation:
                break
    print("YOUR SALT IS.....:")
    for x in range(5):
        print("...")
    print(concation + " " + conanion)


def inputvalidator(message, acceptedinput='string'):
    if acceptedinput == 'password' or acceptedinput == 'pass':
        while True:
            passw = input(message)
            passlength = 6
            minimumdigit = 1
            minimumuppercase = 1
            if len(passw) >= passlength:
                countdigit = 0
                countuppercase = 0
                for x in passw:
                    if x.isdigit():
                        countdigit += 1
                    if x.isupper():
                        countuppercase += 1
                if countdigit >= minimumdigit and countuppercase >= minimumuppercase:
                    confpass = input('Please enter your password again: ')
                    if passw == confpass:
                        return (passw)
                    else:
                        print('Passwords do not match, Please try again')
                else:
                    print(
                        'Password does not meet requirements, Please try again'
                    )
            else:
                print('Password does not meet requirements, Please try again')

    elif acceptedinput == 'email' or acceptedinput == 'mail':
        while True:
            email = input(message)
            if email.count('@') == 1 and email.count('.') == 1:
                return (email)
            else:
                print('Invalid email please enter a valid email!')
    elif acceptedinput == 'yesno':
        yestup = ('y', 'yes', 'ye', 'yeah')
        notup = ('n', 'no', 'nah')
        while True:
            value = input(message)
            value = value.lower()
            if value in yestup:
                return (True)
            elif value in notup:
                return (False)
            else:
                print('Invalid input!, please enter (Y/N) only!')
    elif acceptedinput == 'integers' or acceptedinput == 'integer' or acceptedinput == 'int':
        while True:
            value = input(message)
            try:
                int(value)
            except:
                print('Invalid input, Please enter only integers!')
            else:
                value = int(value)
                return (value)
    elif acceptedinput == 'numbers' or acceptedinput == 'float' or acceptedinput == 'number':
        while True:
            value = input(message)
            try:
                float(value)
            except:
                print('Invalid input, Please enter only numbers!')
            else:
                value = float(value)
                return (value)
    elif acceptedinput == 'strings' or acceptedinput == 'string' or acceptedinput == 'str':
        value = input(message)
        return (value)
    elif type(acceptedinput) == tuple:
        while True:
            value = input(message)
            try:
                int(value)
            except:
                try:
                    float(value)
                except:
                    value = value.lower()
                else:
                    value = float(value)
            else:
                value = int(value)
            if value in acceptedinput:
                return (value)
            else:
                print('Invalid input, Please enter one of these',
                      acceptedinput)
    else:
        for x in range(10):
            print('Invalid pass on type')


def mainmenu(email):
    statement = 'SELECT Name FROM accounts WHERE Email = \'' + email + '\''
    mycursor.execute(statement)
    name = mycursor.fetchall()
    name = name[0][0]
    print('Welcome Back', name + '!')

    statement = "SELECT Accounttype FROM accounts WHERE Email = '" + email + "'"
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

    choice = inputvalidator('Enter a option - ', (1, 2, 3, 4, 5, 6, 7, 8, 9))
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
    elif choice == 7:
        availcheck()
        mainstudent(email)
    elif choice == 8:
        print(
            'You have successfully logged out. You will now be redirected to the homepage!'
        )
        acctMenu()
    elif choice == 9:
        print(
            'Thank you for using our ChemLab Manager! We hope to see you again!'
        )
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

    opt = inputvalidator('Enter option - ', (1, 2, 3, 4, 5, 6, 7, 8, 9))
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
        print(
            'You have successfully logged out. You will now be redirected to the homepage!'
        )
        acctMenu()
    elif opt == 9:
        print(
            'Thank you for using our ChemLab Manager! We hope to see you again!'
        )
        sys.exit()


def bal(email):

    statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\''
    mycursor.execute(statement)
    bal = mycursor.fetchall()
    bal = bal[0][0]

    statement1 = "UPDATE rentedequipment SET datetime2=NOW()"
    mycursor.execute(statement1)
    mydb.commit()
    main = 'SELECT rentedequipment.email, rentedequipment.equipment, rentedequipment.quantity, totalequipment.Price, (time_to_sec(timediff(rentedequipment.datetime2, rentedequipment.datetime))/3600) FROM rentedequipment, totalequipment WHERE (rentedequipment.equipment = totalequipment.EquipmentName) AND rentedequipment.email = "' + email + '"'

    hours = 0
    minutes = 0
    expd = 0

    mycursor.execute(main)
    data = mycursor.fetchall()

    for i in range(len(data)):
        tim = data[i][4] * 60

        if tim > 60:
            hours = tim // 60
            minutes = int(tim % 60)
        if minutes >= 30:
            hours += 1

        expd += data[i][3] * hours + data[i][2]

    bal = bal - expd
    return bal


def rent(email):
    statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\''
    mycursor.execute(statement)
    bal = mycursor.fetchall()
    bal = bal[0][0]
    if bal > 0:
        EquipmentName = (inputvalidator(
            'What equipment would you like to rent - ')).lower()
        statement = "SELECT Price,AvailibleStock FROM totalequipment WHERE EquipmentName = '" + EquipmentName + "'"
        mycursor.execute(statement)
        result = mycursor.fetchall()
        if result == []:
            print(EquipmentName, 'is not a valid Item!')
        else:
            price = result[0][0]
            stock = result[0][1]
            quantity = inputvalidator('Enter Quantity to rent - ', 'int')
            if quantity > result[0][1]:
                print(
                    'We have only', result[0][1], 'of' + EquipmentName +
                    's in stock, Please try again later')
            else:
                res = stock - quantity
                statement1 = 'UPDATE totalequipment SET AvailibleStock = ' + str(
                    res) + ' WHERE EquipmentName = "' + EquipmentName + '"'
                statement2 = "INSERT INTO rentedequipment VALUES('{}' , '{}' , '{}' , NOW(), NOW())".format(
                    email, EquipmentName, str(quantity))

                mycursor.execute(statement1)
                mycursor.execute(statement2)
                mydb.commit()
                print("You have successfully rented", quantity,
                      EquipmentName + '(s)')
    else:
        print("You do not have enough balance to rent an item!")
    mainstudent(email)


def returnequipment(email):
    statement = 'SELECT Balance FROM accounts WHERE Email = \'' + email + '\''
    mycursor.execute(statement)
    bal = mycursor.fetchall()
    bal = bal[0][0]
    statement1 = "UPDATE rentedequipment SET datetime2=NOW()"
    statement2 = "SELECT rentedequipment.equipment, rentedequipment.quantity, (time_to_sec(timediff(rentedequipment.datetime2, rentedequipment.datetime))/3600), totalequipment.Price  FROM rentedequipment, totalequipment WHERE (rentedequipment.equipment = totalequipment.EquipmentName) AND email='{}'".format(
        email)
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
            print(data[i][1], data[i][0] + '(s)')
        option = inputvalidator('Enter choice : ',
                                tuple(range(1,
                                            len(data) + 1)))
        expd = 0
        minutes = 0
        hours = 0
        for i in range(len(data)):
            if data[i][0] == data[option - 1][0]:
                tim = data[i][2] * 60

                if tim > 60:
                    hours = tim // 60
                    minutes = int(tim % 60)
                if minutes >= 30:
                    hours += 1

                expd += data[i][3] * hours + data[i][1]

        bal = bal - expd
        statement1 = "UPDATE accounts SET Balance={} WHERE email='{}'".format(
            bal, email)
        statement2 = "DELETE from rentedequipment WHERE (email='{}' AND equipment='{}' AND quantity={})".format(
            email, data[option - 1][0], data[option - 1][1])
        statement3 = "UPDATE totalequipment SET AvailibleStock=AvailibleStock+{} WHERE EquipmentName = '{}'".format(
            data[option - 1][1], data[option - 1][0])
        mycursor.execute(statement1)
        mycursor.execute(statement2)
        mycursor.execute(statement3)

        mydb.commit()

        print('Item returned successfully!')


def current(email):
    statement1 = "UPDATE rentedequipment SET datetime2=NOW()"
    statement2 = "SELECT equipment, quantity, (time_to_sec(timediff(datetime2, datetime))/3600) FROM rentedequipment WHERE email='{}'".format(
        email)
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
                print('Time rented - ', hours, 'Hour(s) and', int(minutes),
                      'Minutes')
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
        print(x[0], '-', x[1], 'in stock!', '-', 'AED', x[2])


def changepassword(email):
    passw = inputvalidator('Create a new password! - ', 'password')
    passw = encrypt(passw)
    statement = "UPDATE accounts set Password = '{}' WHERE email = '{}'".format(
        passw, email)
    mycursor.execute(statement)
    mydb.commit()
    print(
        'Password changed successfully! You will now be redirected to the homepage!\n'
    )


def main():
  global mydb
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="chemlab")
  global mycursor
  mycursor=mydb.cursor()
  acctMenu()


main()
