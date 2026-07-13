import random
password_length=input('How many digits do you want the password to be? ')
password_length=int(password_length)

numbers="1234567890"
symbols="!@#$%^&*"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_characters=numbers+symbols+lowercase_letters+uppercase_letters
while True:
    print("What do you want in your password? ")
    choice=(input ("numbers=1,symbols=2,lowercase letters=3, uppercase letters=4, all characters=5. you can combine characters eg: 12= numbers and symbols 1234= numbers, symbols and upper and lower case letters  "))

    pool='' 
    if '5' in choice:
      pool= pool+all_characters

    else:
     if '1' in choice:
        pool += numbers
     if '2' in choice:
        pool = pool + symbols
     if '3' in choice:
        pool = pool + lowercase_letters
     if '4' in choice:
        pool = pool + uppercase_letters

    if pool == "":

     print("incorrect question")

    else:
     password= ""
     for _ in range(password_length):
        password = password + random.choice(pool)
     print("your password is: ", password)

    second_password= input('Generate another password? y/n? ')
    if (second_password)==('n'):
     exit()
    else:
      continue
