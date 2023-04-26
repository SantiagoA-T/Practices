from validation_name import validation_of_user
from create_password_bot import validation_pwd

#Validation of names
#user_name = input('Nick name: ')
user_name = input('Nick Name: ')
password = input('Password: ')
save_password = dict([(user_name, password)])

confirmation_pwd = validation_pwd(password)
confirmation_user = validation_of_user(user_name)
print(confirmation_user)
print(confirmation_pwd)