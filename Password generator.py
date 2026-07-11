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

    
""" for _ in range(digits):
 if int(choice)==1:
   password =password + random.choice(numbers)
for _ in range(digits):
 if  int(choice)==2:
  password+= random.choice(symbols)
for _ in range(digits):
  if int(choice)==3:
   password+=random.choice(lowercase_letters)
for _ in range(digits):
  if int(choice)==4:
   password=password+random.choice(uppercase_letters)
for _ in range(digits):
 if int(choice)==5:
  password=password+random.choice(all_characters)

for _ in range(digits):
 if int(choice)==12:
  password=password+random.choice(numbers+symbols)
for _ in range(digits):
 if int(choice)==123:
  password=password+random.choice(numbers+symbols+lowercase_letters)
for _ in range(digits):
 if int(choice)==124:
  password=password+random.choice(numbers+symbols+uppercase_letters)
for _ in range(digits):
 if int(choice)==1234:
  password=password+random.choice(numbers+symbols+lowercase_letters+uppercase_letters)

for _ in range(digits):
 if int(choice)==13:
  password=password+random.choice(numbers+lowercase_letters)
for _ in range(digits):
 if int(choice)==134:
  password=password+random.choice(numbers+lowercase_letters+uppercase_letters)
for _ in range(digits):
 if int(choice)==132:
  password=password+random.choice(numbers+lowercase_letters+symbols)

for _ in range(digits):
 if int(choice)==14:
  password=password+random.choice(numbers+uppercase_letters)
for _ in range(digits):
 if int(choice)==142:
  password=password+random.choice(numbers+symbols+uppercase_letters)
for _ in range(digits):
 if int(choice)==143:
  password=password+random.choice(numbers+lowercase_letters+uppercase_letters)

for _ in range(digits):
 if int(choice)==23:
  password=password+random.choice(symbols+lowercase_letters)
for _ in range(digits):
 if int(choice)==234:
  password=password+random.choice(symbols+lowercase_letters+uppercase_letters)
for _ in range(digits):
 if int(choice)==231:
  password=password+random.choice(numbers+lowercase_letters+symbols)

for _ in range(digits):
 if int(choice)==24:
  password=password+random.choice(symbols+uppercase_letters)
for _ in range(digits):
 if int(choice)==241:
  password=password+random.choice(symbols+numbers+uppercase_letters)
for _ in range(digits):
 if int(choice)==243:
  password=password+random.choice(symbols+lowercase_letters+uppercase_letters)

for _ in range(digits):
 if int(choice)==34:
  password=password+random.choice(lowercase_letters+uppercase_letters)
for _ in range(digits):
 if int(choice)==341:
  password=password+random.choice(numbers+lowercase_letters+uppercase_letters)
for _ in range(digits):
 if int(choice)==342:
  password=password+random.choice(symbols+lowercase_letters+uppercase_letters)

for _ in range(5):
 print("your password is: ", (random.choice(password) ))"""
