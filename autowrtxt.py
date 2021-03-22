# Python 3.8.6
print(f"""{__file__}

'''Auto write text with pyautogui'''

Requirements: 'pyautogui' (& 'pyperclip' for Option 4)

Option 1. Write contents of a text file
Option 2. Write contents of the text provided by you
Option 3. Write contains of this file
Option 4: Write contains of the clipboard! (Default)

NOTE: Edit source code to select different option.
""")

from time import sleep
try: from pyautogui import write
except ModuleNotFoundError as e:
    exit(f"{e}\nInstall 'pyautogui' first")

option = 4
txttowr = ""

if option == 1:
    print("Option 1. Writ contents of a text file")
    try:
        filename = input("Enter tex file path: ").strip('"')
        open(filename)
    except KeyboardInterrupt: exit('Abort!')
    except FileNotFoundError as e: exit(e)
    with open(filename, 'rt') as fh:
        for line in fh.readlines(): txttowr += line
elif option == 2:
    print("Option 2. Write contents of the text provided by you")
    txttowr = """Your text here"""
    # txttowr = input('Enter text to write: ').strip()
elif option == 3:
    print("Option 3. Write contains of this file")
    with open(__file__, 'rt') as fh:
        for line in fh.readlines(): txttowr += line
elif option == 4:
    print("Option 4: Writing contains of the clipboard!")
    try: import pyperclip
    except ModuleNotFoundError as e:
        exit(f"\n{e}\nInstall 'pyperclip' first")
    txttowr = pyperclip.paste()
    if len(txttowr) < 1:
        txttowr = "Your clipboard is empty!"
        print(txttowr)

if len(txttowr) > 100: print(
    f"The length of text to write is {len(txttowr)}.")
try: input('Enter [RETURN] to continue..')
except KeyboardInterrupt: exit('Abort!')

try:
    print('Quickly move the cursor to a text field.\nYou have 5 sec. Then I start to write.')
    sleep(5)
    print('Now writing..', end="")
    write(txttowr, interval=0.075)
    print('. Done!')
except KeyboardInterrupt: exit('Abort!')


exit('[ Done ] No interruptions!')
# The End.
