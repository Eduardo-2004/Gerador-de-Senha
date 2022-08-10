import random
import string

def password_generator(length_pass):
    ascii_option = string.ascii_letters
    number_option = string.digits
    punt_options = string.punctuation
    options = ascii_option + number_option + punt_options

    password_user = ""
    #Range == estrutura de lista
    for digit in range(0, length_pass):
        digit = random.choice(options)
        password_user = password_user + digit
    
    return password_user

choice_user = input("A senha será composta por quantos digitos? ")

if  choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Digitos inválidos!")
    quit()

response = password_generator(length_pass = choice_user)
print("Senha: " + response)


        