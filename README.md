# SimpleLoginSystem

SimpleLoginSystem is a small terminal program written in Python that allows you log in and sign up
to your account where you can view your account details such as: username, password, and your hint to the password.
It uses PostgreSQL database to perform simple authentification by comparing the password in the database to the one
provided in the terminal. It allows you to set a new password in case you forgot it using the password hint.

## Contents:

1. ### main.py: 

it executes the program and uses the pcycopg2 module to make queries to the PostgreSQL database. It also uses functions signUp() and logIn() imported from myFunctions.py file.

2. ### myFunctions.py: 
it contains functions such as

- logIn()
- signUp()
- incorrectInput()
- insideAccount()
- addProfile()
- forgotPassword()


