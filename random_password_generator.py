import string
import random

ascii_letters = string.ascii_letters  # Concatenation of the ascii (upper and lowercase) letters
ascii_lowercase = string.ascii_lowercase  # All lower case letters
ascii_uppercase = string.ascii_uppercase  # All Upper case letters
digits = string.digits   # The string ‘0123456789’.
punctuation = string.punctuation   # String of ASCII characters which are considered special characters

necessary_chars = [ascii_lowercase, ascii_uppercase, digits, punctuation]
finish = False
while (not finish):
    password = ""
    password_len = input("What is the length of password to generate (min. 6): ")

    try:
        if (int(password_len) < 6):
            print("The length of password is too short. Try again")
            continue
    except ValueError:
        print("The typed text is not a decimal number. Try again")
        continue

    while (True):
        for i in range(0, int(password_len)):
            rand_set = random.randint(0, len(necessary_chars) - 1)
            # print("rand_set " + str(rand_set))
            password += necessary_chars[rand_set][random.randint(0, len(necessary_chars[rand_set]) - 1)]

        is_used = []
        for n in range(0, len(necessary_chars)):
            is_used.append(any(char in password for char in necessary_chars[n]))

        # if (any(char in password for char in necessary_chars[0]) and
        #    any(char in password for char in necessary_chars[1]) and
        #    any(char in password for char in necessary_chars[2]) and
        #    any(char in password for char in necessary_chars[3])):
        #     print("Your generated password is: " + password)
        #     finish = True
        #     break
        if all(is_used):
            print("Your generated password is: " + password)
            finish = True
            break
        else:
            # print("Clearing password")
            password = ""
