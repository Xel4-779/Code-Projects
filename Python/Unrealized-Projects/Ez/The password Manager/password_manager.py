import getpass

import json
from pathlib import Path
from cryptography.fernet import Fernet

DATA_FILE = Path(__file__).with_name("passwords.json")
KEY_FILE = Path(__file__).with_name("secret.key")

password_manager = {}


def return_key():
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()
    else:
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        return key
        

def load_passwords():
    global password_manager

    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            password_manager = json.load(file)


def save_passwords():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(  password_manager , file , indent = 4  )

key = return_key()
cipher = Fernet(key)


def create_account():
      

    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    password_manager[username] = cipher.encrypt(password.encode()).decode()
    print("----------------------------------------------")

    save_passwords()



def login():
    username = input("Enter your username: ")
    
    password = getpass.getpass("Enter your password: ") 
    encrypted_password =cipher.encrypt(password.encode()).decode()

    if username in password_manager and password_manager[username] == encrypted_password:
        
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


def decode_password_from( current_account ):
    if password_manager[current_account] != None:

        password =password_manager[current_account]
        decrypted_password = cipher.decrypt(password.encode()).decode()
        print(decrypted_password)

    else:
        print("Nonexisting account")


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