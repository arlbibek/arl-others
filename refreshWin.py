print("""Name: refreshWin.py

'''Refresh windws 'n' numbers of times.'''

Requirements: pyautogui
""")

# TODO: Check if the program is being run on windows or not.

try: import pyautogui
except ModuleNotFoundError as e: exit(e)


def refreshWin():
    '''Refresh windows n numbers of times'''
    while True:
        try:
            n = int(input('How many times do you want to refresh windows?\n: '))
            print(f'Windows will be refreshed {n} times.')
            input('Press [RETURN] to continue..')
            break
        except ValueError:
            print("Enter an positive Integer!")
            continue
        except KeyboardInterrupt: exit('Abort!')
    if not n < 1:
        pyautogui.hotkey('win', 'd')
        for i in range(n):
            pyautogui.rightClick(x=1442, y=190)
            pyautogui.click(x=1472, y=253)
        pyautogui.hotkey('win', 'd')
        print('Refreshed', i + 1, 'times.')


refreshWin()

print("\n[ Done ]")
exit('\nBye..')

# The End.
