import psycopg2

def logIn(cur, conn):
    username = input("username: ")
    password = input("password: ")
    
    cur.execute("SELECT * FROM users\n"
    "WHERE username = %s AND password = %s",
    (username, password))

    retrieved_user = cur.fetchone()
    
    if retrieved_user == None:
        incorrectInput(cur, conn)
    else:
        insideAccount(username, cur, conn)


def incorrectInput(cur, conn):
    option = input("\nincorrect username or password\n"
    "1. log in\n"
    "2. exit the program\n"
    "3. forgot password?\n"
    "choose an option(1/2/3): ")
    
    if option == '1':
        logIn(cur, conn)
    elif option == '2':
        exit()
    else:
        forgotPassword(cur, conn)


def startOver(cur, conn):
    conn = psycopg2.connect("dbname=my_database "
    "user=postgres "
    "password=postgres")

    cur = conn.cursor()

    option = input("1. sign up\n"
    "2. log in\n"
    "choose an option(1/2): ")

    if option == '1':
        signUp(cur, conn)
    else:
        logIn(cur, conn)

    cur.close()
    conn.close()


def insideAccount(username, cur, conn):
    print(f"you logged in as {username}")

    option = input("1. view profile\n"
    "2. log out\n"
    "choose an option(1/2): ")

    if option == '1':
        cur.execute("SELECT * FROM users\n"
        "WHERE username = %s", (username,))

        user = cur.fetchone()

        print(f"username: {user[1]}\n"
        f"password: {user[2]}\n"
        f"authentification: {user[3]}")

        option = input("1. log out(yes/no):")

        if option == 'yes':
            print("you logged out\n")
            logIn(cur, conn)
        else:
            insideAccount(username, cur, conn)
    else:
        print("you logged out successfully")
        startOver(cur, conn)


def signUp(cur, conn):
    is_unique = True
    username = input("username: ")
    password = input("password: ")
    check_password = input("repeat password: ")
    authentification = input("the name of the city you were born: ")

    cur.execute("SELECT username FROM users;")

    usernames = cur.fetchall()

    for u in usernames:
        if u[0] == username:
            print("the user with this username already exists")

            option = input("1. sign up\n"
            "2. exit the program\n"
            "choose an option(1/2): ")

            if option == '1':
                signUp(cur, conn)
            else:
                exit()
            is_unique = False
    
    if is_unique == True:
        if password == check_password:
            addProfile(username, password, authentification, cur, conn)
        else:
            print("passwords does not match")

            opt = input("1. sign up\n"
            "2. exit the program\n"
            "choose an option(1/2): ")

            if opt == '1':
                signUp(cur, conn)
            else:
                exit()


def addProfile(username, password, authentification, cur, conn):
    cur.execute("INSERT INTO users(username, password, authentification) \
                VALUES(%s, %s, %s);", (username, password, authentification))

    conn.commit()


def forgotPassword(cur, conn):
    username = input("username: ")

    cur.execute("SELECT * FROM users \
        WHERE username = %s", (username,))
    
    user_tuple = cur.fetchone()
    
    if user_tuple == None:
        print("there is no such username")
    else:
        authentification = input("city you were born: ")

        if authentification == user_tuple[3]:
            new_password = input("provide a new password: ")

            cur.execute("UPDATE users SET password = %s \
                WHERE username = %s",(new_password, username))

            conn.commit()
        
            print("the password changed succesfully\n")
        else:
            print("incorrect input\n")

            option = input("1. try again\n"
            "2. exit the program")

            if option == '1':
                forgotPassword(cur, conn)
            else:
                exit()

        option = input("1. log in\n"
        "2. exit the program\n"
        "choose an option(1/2): ")

        if option == 1: 
            logIn(cur, conn)
        else:
            exit()