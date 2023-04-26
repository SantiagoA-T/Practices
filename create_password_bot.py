import random 

password_created = []

def create_password():
        #function that create it the password 
        letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLMZNXBCV'
        nums = '1234567890'
        caracters = '~!@#$%^&*_-+)[(}{`]=\|"?>./,<:;'
        while len(password_created) <= 17:
          letter, num, carac = random.choice(letters), random.choice(nums), random.choice(caracters)
          password_created.append(num)
          password_created.append(letter)
          password_created.append(carac)
        random.shuffle(password_created)
        return ''.join(password_created)

def validation_pwd(pwd):
      pwdd = str(pwd)
      islum = 0
      issuper = 0
      islower = 0
      isdigit = 0
      isapace = 0 
      #total = islum + issuper + islower + 
      for letter in pwdd:
            if len(pwdd) < 8:
                  'Should have at lease 8 caracters'
            if letter.isalnum() == True:
                  if letter.isupper() == True:
                        issuper += 1 
                  if letter.islower() == True:
                        islower += 1  
                  if letter.isdigit() == True:
                        isdigit += 1
            else:
                  islum += 1
            if letter.isspace() == False:
                  isapace += 1                  
      if islum and issuper and islower and isdigit and isapace > 0:
            return 'Valid Password'
      else:
            return 'The password chosen its not safe'

if __name__ == '__main__':
      call_pass = create_password()
      print(validation_pwd(call_pass))
#validation_pwd('fdertgyhja45')