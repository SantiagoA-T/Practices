import random
from create_password_bot import create_password

def crear_lista_names():
                #function that create an email
                names = open('names.txt', 'r')
                read_lines = names.read()
                lower = read_lines.lower()
                split_ = lower.split(',')
                nums_for = '123456789'
                gmail = '@gmail.com'
                for i in split_:
                    nums_generate = random.choices(nums_for, weights=None, k=4)
                    mess = random.sample(i, k=len(i))
                    random.shuffle(split_)
                    nums_str = ''.join(nums_generate)
                    mess_list = ''.join(mess)
                    final = mess_list + nums_str + gmail
                    break
                return final

funct_call = crear_lista_names()
print(funct_call)
password_call = create_password()
