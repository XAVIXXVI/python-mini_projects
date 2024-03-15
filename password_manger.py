from cryptography.fernet import Fernet

print("Welcome to the password manager.")
pwd = input("What is the master password? ")


def write_key():
    """
    This function used to create the key once you created
    the key.key file comment it out
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return None


def load_key():
    with open("key.key", 'rb') as load_key_file:
        key = load_key_file.read()
    return key

key = load_key() + pwd.encode()
fer = Fernet(key)
def view():
    while True:
            m_pwd = input("Please enter your master password: ")
            if m_pwd == pwd:
                with open("passwords.txt", 'r') as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        user, passw = data.split("|")
                        print(f"User name: {user} and password: {fer.decrypt(passw.encode()).decode()}")
                break
            else:
                print("Wrong master password")
                continue
    return None


def add():
    while True:
        m_pwd = input("Please enter your master password: ")
        if m_pwd == pwd:
            user_name =  input("Pleas enter the username you want to add: \n ")
            user_pwd = input("Pleas enter the password you want to add: \n ")
            with open("passwords.txt", "a") as f:
                f.write(user_name + "|" + fer.encrypt(user_pwd.encode()).decode() + "\n")

            print("Password added successfully")

            break
        else:
            print("Wrong master password")
            continue
    return None


while True:
    mode = input("If you want to add new password please type 'add' \nif you want to view your passwords please type 'view' \nif you want to quit please enter 'q': \n ")
    if mode =="q":
        break

    if mode == "add":
        add()
    elif mode == "view":
         view()
    else:
        print("Please enter a valid option")
        continue
