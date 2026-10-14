from random import randint, choice
import string



def generate_password(length: int):

    password_result = ""


    for i in range(0,length):

        char = choice(string.ascii_lowercase)

        password_result = password_result + char
    return password_result




password = generate_password(7)
print(password)
