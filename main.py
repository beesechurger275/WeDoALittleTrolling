from pynput import keyboard
import pyperclip
import re

with open("copy.txt", "r") as file:
    fileContents = file.read()

regBreak = re.findall(r"\S.{0,100}(?<=\S)(?!\S)", fileContents)
print(regBreak)

index = 0
def on_press(key):
    global index
    if key == keyboard.Key.enter:
        try:
            pyperclip.copy(regBreak[index])
        except IndexError:
            pyperclip.copy("#")
            print("done with copy paste")
        index += 1
        print(f"index: {index}")
    elif key == keyboard.Key.page_up:
        index += 1
        print(f"raised index to {index}")
        pyperclip.copy(regBreak[index])
    elif key == keyboard.Key.page_down:
        index -= 1
        print(f"lowered index to {index}")
        pyperclip.copy(regBreak[index])

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()