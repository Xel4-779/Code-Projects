import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter a username: ")
    password = input("Enter password: ")
    #password = getpass.getpass("Enter a password: ")

    password_manager[username] = password

def login():
    username = input("Enter your username: ")
    
    password = getpass.getpass("Enter your password: ")
    

    if username in password_manager and password_manager[username] == password:
        
        print("Login successful!")
        print(password)
    else:
        print("Invalid username or password.")
        print(password)

def main():
    while True:
        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("4. Retrieve Password")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
           
            login()
        elif choice == '3':
            break
        elif choice == '4':
            
            for username in password_manager:
                print(f" Password : {password_manager[username]}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()