import getpass

import json
from pathlib import Path
from cryptography.fernet import Fernet

DATA_FILE = Path(__file__).with_name("passwords.json")
KEY_FILE = Path(__file__).with_name("secret.key")

parent_accounts = {}
password_manager = {}


def return_key():
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()
    else:
        new_key = Fernet.generate_key()
        KEY_FILE.write_bytes(new_key)
        return new_key
        

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
    encrypted_password = cipher.encrypt(password.encode()).decode()

    if username in password_manager and password_manager[username] == encrypted_password:
        
        print("Login successful!")
        print("----------------------------------------------")
    else:
        print("Invalid username or password.")
        print("----------------------------------------------")

def change_password():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your current password: ")
    encrypted_password = cipher.encrypt(password.encode()).decode()


    if username in password_manager and password_manager[username] == encrypted_password:
        new_password = getpass.getpass("Enter your new password: ")
        password_manager[username] = cipher.encrypt(new_password.encode()).decode()


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


def retrieve_all_passwords():
    print("----------------------------------------------")
    print("Currently stored passwords, there are " + str(len(password_manager)) + " accounts stored: ")
    i = 1
    for account in password_manager:
        decrypted_password = cipher.decrypt(password_manager[account].encode()).decode()
        print(str(i) + ". " + account[:1].upper() + account[1:] + " : " + decrypted_password)
        i += 1

    print("----------------------------------These are all the passwords stored.")



def main():

    load_passwords()

    while True:
        print("----------------------------------------------")

        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")
        print("3. Retrieve Password")
        print("4. Change Password")
        print("5. Retrieve All Passwords")

        print("Any other key to exit")
        print("----------------------------------------------")


        choice = input("Enter your choice: ")

        match choice:
            case '1':
                create_account()
            case '2':
                login()
            case '3':
                decode_password_from(input("Enter the username to retrieve the password: "))
            case '4':
                change_password()
            case '5':
                retrieve_all_passwords()
            case _:
                break




if __name__ == "__main__":
    main()