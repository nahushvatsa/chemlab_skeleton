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
                        return(passw)
                    else:
                        print('Passwords do not match, Please try again')
                else:
                    print('Password does not meet requirements, Please try again')
            else:
                print('Password does not meet requirements, Please try again')

    elif acceptedinput == 'email' or acceptedinput == 'mail':
        while True:
            email = input(message)
            if email.count('@') == 1 and email.count('.') == 1:
                return(email)
            else:
                print('Invalid email please enter a valid email!')
    elif acceptedinput == 'yesno':
        yestup = ('y', 'yes','ye','yeah')
        notup = ('n', 'no','nah')
        while True:
            value = input(message)
            value = value.lower()
            if value in yestup:
                return(True)
            elif value in notup:
                return(False)
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
                return(value)
    elif acceptedinput == 'numbers' or acceptedinput == 'float' or acceptedinput == 'number':
        while True:
            value = input(message)
            try:
                float(value)
            except:
                print('Invalid input, Please enter only numbers!')
            else:
                value = float(value)
                return(value)
    elif acceptedinput == 'strings' or acceptedinput == 'string' or acceptedinput == 'str':
        value = input(message)
        return(value)
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
                return(value)
            else:
                print('Invalid input, Please enter one of these', acceptedinput)
    else:
        for x in range(10):
            print('Invalid pass on type')
