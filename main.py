import psycopg2
from myFunctions import signUp, logIn

def start():
    conn = psycopg2.connect("dbname=my_database user=postgres \
        password=postgres")
    cur = conn.cursor()

    optionStart = input("1. Sign up\n"
                    "2. Log in\n"
                    "Choose an option(1/2): ")

    if optionStart == '1':
        signUp(cur, conn)
    else:
        logIn(cur, conn)

    cur.close()
    conn.close()

start()