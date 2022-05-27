# Refresh windows 'n' numbers of times.
# Requirements: pyautogui

def refreshWin(n):
    '''Refresh windows n numbers of times
    Requrement: pyautogui'''

    # Identifying platform and working accordingly
    from platform import system
    if not system().lower().startswith('win'):
        print("[ Aborted! ] Couldn't refresh on a none Windows system.")
    else:
        from pyautogui import hotkey, rightClick, click
        if not n < 1:
            hotkey('win', 'd')
            for i in range(n):
                rightClick(x=1442, y=190)
                click(x=1472, y=253)
            hotkey('win', 'd')
            print('Refreshed', i + 1, 'time(s).')


def main():
    from sys import argv
    from os.path import basename
    try:
        if len(argv) > 1:
            refreshWin(int(argv[1].strip().strip('-')))
        else:
            refreshWin(
                int(input('How many times do your want refresh windows?\n: ')))
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        exit('Abort!')


if __name__ == '__main__':
    main()

# The End.
