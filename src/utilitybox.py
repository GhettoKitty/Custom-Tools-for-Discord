import time
from pynput.keyboard import Key, Controller

print("""This is a spammer that works on any platform.
It simulates keyboard input. Make sure to click into a text field after starting the script.
All time values are treated as seconds.
Made by 6A31 - https://github.com/ScobraScope

Please be aware that setting the Delay between messages too low can cause your pc to lag / freeze""")


des1 = int(input("How long should the script wait before starting to spam? >>> "))
des2 = int(input("How many messages should get send? >>> "))
des3 = str(input("Message: >>> "))
des4 = float(input("Delay between messages: "))


time.sleep(des1)
keyboard = Controller()
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
i = 1
des2 += 1
while i < (des2):
    keyboard.type(des3 + " " + str(i))
    enter()
    i += 1
    time.sleep(des4)