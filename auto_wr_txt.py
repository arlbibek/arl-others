# local imports
from get_input import get_input
from get_path import get_filepath


def get_txt_clipboard():
    """Returns contains of the clipboard using 'pyperclip'"""

    import pyperclip

    txt_to_wr = pyperclip.paste()
    if len(txt_to_wr) < 1:
        txt_to_wr = "Your clipboard is empty!"

    return txt_to_wr


def get_txt_file():
    """Prompts to provide a valid file path to the user and return the contents of that file."""

    txt_to_wr = ""
    filename = get_filepath()

    with open(filename, 'rt') as fh:
        for line in fh.readlines():
            txt_to_wr += line

    if len(txt_to_wr) < 1:
        txt_to_wr = "Your file is empty!"

    return txt_to_wr


def get_txt_user():
    """Prompts user to provide contents and returns that contents"""

    txt_to_wr = get_input("Enter text to write")
    if txt_to_wr is None:
        txt_to_wr = "Got 'None' from the  user"

    return txt_to_wr


def auto_wr_txt(text, speed=0.075):
    """"""

    from pyautogui import write
    from time import sleep

    try:
        print(f"The length of text to write is {len(text)}.")
        input('Enter [RETURN] to continue..')

        print("\n⚠")
        print('Quickly move the cursor to a text field.\nYou have 5 sec. Then I start to write.')
        sleep(5)
        print('Now writing..', end="")
        write(text, interval=speed)
        print('. Done!')
    except KeyboardInterrupt:
        print("[ Keyboard Interrupt ] Aborted!")


if __name__ == "__main__":
    print(f"""{__file__}

'''Auto write text with pyautogui'''

Requirements: 'pyautogui' (& 'pyperclip' for Option 1)
""")
    menu = {}
    menu[1] = "Write contains of the clipboard."
    menu[2] = "Write contents of the text provided."
    menu[3] = "Write contents of a text file."

    while True:
        for k, v in menu.items():
            print(f"Option {k}: {v}")
        user_option = get_input("\nChoose and select an option", num=True)
        if user_option == None:
            break
        if user_option not in menu.keys():
            print(
                f"\nExpected one of the {[k for k in menu.keys()]}, got '{user_option}'. Please try again!\n")
            continue
        else:
            if user_option in menu.keys():
                print()
                print(f"Option {user_option}:  {menu[user_option]}")
                print()
                if user_option == 1:
                    txt_to_wr = get_txt_clipboard()
                    auto_wr_txt(txt_to_wr)
                elif user_option == 2:
                    txt_to_wr = get_txt_file()
                    auto_wr_txt(txt_to_wr)
                elif user_option == 3:
                    txt_to_wr = get_txt_user()
                    auto_wr_txt(txt_to_wr)
            break
