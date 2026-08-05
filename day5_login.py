# User Login Validator

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        
        print("Login successful! Welcome.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid username or password. Attempts left: {attempts}")
        else:
            print("Account locked. Too many failed attempts.")