import getpass
import hashlib
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("passwords.json")

password_manager = {}


def load_passwords():
    global password_manager

    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            password_manager = json.load(file)


def save_passwords():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(  password_manager , file , indent = 4  )



def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    password_manager[username] = password
    print("----------------------------------------------")

    save_passwords()



def login():
    username = input("Enter your username: ")
    
    password = getpass.getpass("Enter your password: ")
    

    if username in password_manager and password_manager[username] == password:
        
        print("Login successful!")
        print("----------------------------------------------")
    else:
        print("Invalid username or password.")
        print("----------------------------------------------")

def change_password():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your current password: ")
    if username in password_manager and password_manager[username] == password:
        new_password = getpass.getpass("Enter your new password: ")
        password_manager[username] = new_password


        save_passwords()


        print("Password changed successfully.")
        print("----------------------------------------------")
    else:
        print("Username or password is incorrect.")
        print("----------------------------------------------")


def main():

    load_passwords()

    while True:
        print("----------------------------------------------")

        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")

        print("4. Retrieve All Passwords")
        print("5. Change Password")


        print("Any other key to exit")
        print("----------------------------------------------")


        choice = input("Enter your choice: ")

        match choice:
            case '1':
                create_account()
            case '2':
                login()
            case '4':
                load_passwords()
                for username in password_manager:
                    print(f" Username: {username}, Password: {password_manager[username]}")
            case '5':
                change_password()
            case _:
                break


if __name__ == "__main__":
    main()