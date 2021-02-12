# Refresh windws 'n' numbers of times.
# Requirements: pyautogui

def refreshWin(n):
    '''Refresh windows n numbers of times
    Requrement: pyautogui'''
    from pyautogui import hotkey, rightClick, click
    from platform import system as pfsys

    if pfsys().lower().startswith('windows'):
        if not n < 1:
            hotkey('win', 'd')
            for i in range(n):
                rightClick(x=1442, y=190)
                click(x=1472, y=253)
            hotkey('win', 'd')
            print('Refreshed', i + 1, 'time(s).')
    else: print("Couldn't refresh on a none Windows system.")


if __name__ == '__main__':
    from sys import argv
    from os.path import basename
    print(f"""Name: {basename(__file__)}

'''Refresh windws 'n' numbers of times.'''

Requirements: pyautogui
""")

    try:
        if len(argv) > 1: refreshWin(int(argv[1].strip().strip('-')))
        else: refreshWin(int(input('How many times do your want refresh windows?\n:')))
    except Exception as e: print(e)
    except KeyboardInterrupt: exit('Abort!')

# The End.
