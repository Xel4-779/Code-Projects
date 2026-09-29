from pathlib import Path
import os


SALT_FILE = Path(__name__).with_name("new_salt.bin")

def random_salt():
    if SALT_FILE.exists() :
        return SALT_FILE.read_bytes()
    else:
        salt = os.urandom(16)
        SALT_FILE.write_bytes(salt)
        return salt


print("------------------------------------------------------------")
print("\n")
print("Random salt:  " + random_salt().hex())
print("\n")
print("------------------------------------------------------------")