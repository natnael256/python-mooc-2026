from random import choice 
import string


def generate_strong_password(length: int, include_digits = True, punct = True):
    password_result = ""

    for i in range(1, length):
        char = ""
        if include_digits  == False and punct == False:

            char = choice(string.ascii_lowercase)

        if include_digits == True and punct ==True:

            char = choice(string.punctuation + string.ascii_lowercase + string.digits)


            any(char in string.punctuation for char in password_result)

            any(char in string.digits for char in password_result)

            any(char in string.ascii_lowercase for char in password_result)












        password_result = password_result + char


    return password_result




if __name__ == "__main__":
    fPassword  = generate_strong_password(8, True, True)
    # fPassword  = generate_strong_password(8, False, False)
    # fPassword  = generate_strong_password(8, False, True)
    # fPassword  = generate_strong_password(8, True, False)
    print(fPassword)