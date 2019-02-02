def validate_user(username):
    '''
        username should be made up of alphabets only
        return True if username is valid
        return False if username is invalid
    '''
    return True

def validate_password(passwd):
    '''
        passwd should be atleast 8 characters long
        passwd should contain alphabets and digits
        return True if passwd is valid
        return False if passwd is invalid
    '''
    return True

def rate_passwd(passwd):
    '''
        print Weak if passwd has less than 3 digits
        print Good if passwd has more than 2 digits
        print Strong if passwd begins with digit and is not Weak
    '''

# Main
uname = get_username()
if validate_user(uname):
    pswd = get_passwd()
    if validate_password(pswd):
        print("Your password is ", rate_passwd(pswd))
    else:
        print("Your password should be atleast 8 characters long and contain alphabets and digits")
else:
    print("Your username should only contain alphabets")
