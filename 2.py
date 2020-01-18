import re

def usernameValidity(username):
    if re.match(r'^(?=.*?^[a-z])(?=.*?[0-9])(?=.*?_).{5,12}$', username):
        return True
    else:
        return False

def passwordValidity(password):
    if re.match(r'^(?=.*?[A-Z]{5})(?=.*?[0-9]{1})(?=.*?[#?!@$%^&*-]{1}).{7,7}$', password):
        return True
    else:
        return False

#diawali huruf kecil, tidak ada huruf besar, spesial karakter (_), dan min 5 - 12 kar
listUsername = ['amalfajrin','amale_3rer_e','amal456']
#5 huruf besar, 1 simbol, 1 angka
listPassword = ['AMALF2!','AMALf2!','4LAMAM!']

user = 1
pwd = 1

for username in listUsername:
    if usernameValidity(username) == True:
        print ("Username {0} memenuhi syarat".format(str(user)))
    else:
        print ("Username {0} tidak memenuhi syarat".format(str(user)))
    user += 1
    
for password in listPassword:
    if passwordValidity(password) == True:
        print ("Password {0} memenuhi syarat".format(str(pwd)))
    else:
        print ("Password {0} tidak memenuhi syarat".format(str(pwd)))
    pwd += 1