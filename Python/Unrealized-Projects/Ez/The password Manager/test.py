from cryptography.fernet import Fernet

key = Fernet.generate_key()
cypher = Fernet(key)

password = input("Enter a password to encrypt: ")

encripted_password = cypher.encrypt(password.encode()).decode()

print("----------------------------------------------")
print("Encrypted password: " + encripted_password)
print("----------------------------------------------")
print("Decrypted password: " + cypher.decrypt(encripted_password.encode()).decode())
