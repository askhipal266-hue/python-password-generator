import streamlit as st
import random
password_length=st.number_input('How many digits do you want the password to be? ')
password_length=int(password_length)

numbers="1234567890"
symbols="!@#$%^&*"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_characters=numbers+symbols+lowercase_letters+uppercase_letters

include_numbers = st.checkbox("Include Numbers")
include_symbols = st.checkbox("Include Symbols")
includelowercase_letters = st.checkbox("Include Lowercase Letters")
include_uppercase_letters = st.checkbox("Include Uppercase Letters")
include_numbers_all_characters = st.checkbox("Include All Characters")

pool=''  
if include_numbers_all_characters:
     pool= pool+all_characters
else:
     if include_numbers :
        pool += numbers
     if include_symbols :
        pool = pool + symbols
     if includelowercase_letters :
        pool = pool + lowercase_letters
     if include_uppercase_letters:
        pool = pool + uppercase_letters
if st.button("Generate Password"):
            if pool == "":
                st.error("Please select at least one character type!")
            else:
                password= ""
                for _ in range(password_length):
                     password = password + random.choice(pool)
                st.write("your password is: ", password)

'''second_password= st.text_input('Generate another password? y/n? ')
if (second_password)==('n'):
    st.write('Applicationn stopped')
    st.stop()'''
