############################################
#
#               DISCORD TOOL UTILITY
#
# Support:
# GitHub- https://github.com/GhettoKitty 
#
############################################


from keyboard import press
from time import sleep
from discord import utility
from utility import webhook
import json
import pyautogui, os
import discord

def end(): #Exit function with a message
    print('\nThanks for using this tool\nif you have any issues, contact me on discord or github')
    exit(0)

def main(): #main function
    os.system('cls')
    print('''                                 
    \nThis is a very simple discord tool utility.
Instructions: Just type your spam text and number of time to spam, hit enter and point your cursor to the input box, the spam will begin in 10 seconds.

NOTE: THIS TOOL CAN CAUSE A CHAOS IF NOT USED IN THE RIGHT WAY. IN SIMPLE WORDS IT WILL SPAM ANYWHERE YOUR CURSOR IS AT, SO MAKE SURE YOUR CURSOR IS IN THE RIGHT INPUT BOX

Support:
Discord- https://discord.gg/3nfQadt
GitHub- https://github.com/Assassinumz
''')#Tool banner with instructions and contact info

    spam = input("Enter your spam text:\n-> ") #Gets the input from the user and stores it as the spam text 
    num = input("\nNumber of times to spam (Leave it for if you want it to spam forever):\n-> ") #sets number of time to spam
    if num == "": #if num is blank sets num to 999999... you won't let this loop that many times would you ?
        num = 999999

    print('\nThe spam will begin in 10 seconds... BRACE YOURSELF !!!\n')#BRACE YOURSELF !!!!
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime\n\n")#how to stop the chaos
    sleep(10)#gives time for lazy users to point towards the input box

    for _ in range(int(num)):
        sleep(0.3)#stop the spam for 0.3 seconds every loop
        pyautogui.typewrite(spam) #types the spam text in the input box
        press('enter') # hits enter
    
    end()#calls the end function

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()


try:
    while True:
        while keyboard.is_pressed(KeyToHold):
            keyboard.send(' ')
            print(f"{KeyToHold} is being held")
            time.sleep(DelayInSeconds)
except:
    pass
finally:
    keyboard.unhook_all()

# keep window alive if program stops
k=input("The program has failed. This could be because you entered an invalid number for the delay, entered an invalid key, or the key is not surrounded by two apostrophes. Press return to exit.")
