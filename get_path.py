print(f"""{__file__}

'''Get file/directory path from the user'''
""")


def getfilepath(msg="Enter file path: "):
    '''Asks for a file path to the user then,
    Returns absolute path of the file if the file exist.'''
    from os.path import abspath, exists, isfile
    while True:
        try:
            path = input(f"\n{msg}").strip().strip("'").strip('"')
        except KeyboardInterrupt:
            exit('Abort!')
        if len(path) < 1:
            continue
        if exists(path):
            if isfile(path):
                return(abspath(path))
            else:
                print(f"'{path}' is not a file.")
        else:
            print(f"Couldn't locate file: {path}.")
        print("Try again!")


def getdirpath(msg="Enter file path: "):
    '''Asks for a directory path to the user then,
    Returns absolute path of the directory if the directory exists.'''
    from os.path import abspath, exists, isdir
    while True:
        try:
            path = input(f"\n{msg}").strip().strip("'").strip('"')
        except KeyboardInterrupt:
            exit('Abort!')
        if len(path) < 1:
            path = '.'
        if exists(path):
            if isdir(path):
                return(abspath(path))
            else:
                print(f"'{path}' is not a directory path.")
        else:
            print(f"Couldn't locate: {path}.")
        print("Try again!")


# TEST
def getOption():

    menu = {}
    menu[1] = 'Get file path'
    menu[2] = 'Get directory path'
    menu[3] = 'Exit'
    while True:
        print()
        for k, v in menu.items():
            print(f'{k} : {v}')

        try:
            option = int(input(f"Choose: ").strip())
        except KeyboardInterrupt:
            exit('Abort!')
        except ValueError:
            print(
                f'\n[ Invalid input ] Choose one of {[k for k in menu.keys()]}')
            continue

        if option in [k for k in menu.keys()]:
            return option

        print(
            f'\n[ Value out of range ] Choose one of {[k for k in menu.keys()]}')


if __name__ == "__main__":
    from os.path import basename

    choosen = getOption()

    if choosen == 1:
        path = getfilepath()
        print(f"\nFile path: {path}\nFile name: {basename(path)}")
    elif choosen == 2:
        path = getdirpath()
        print(f"\nDirectory path: {path}\nDirectory name: {basename(path)}")
    else:
        exit('Bye..')
# The end.
