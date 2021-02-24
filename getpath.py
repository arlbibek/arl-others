def filepath():
    '''Asks for a file path to the user then,
    Returns absolute path of the file if the file exist.'''
    from os.path import abspath, exists, isfile
    while True:
        try: path = input("\nEnter file path: ").strip().strip("'").strip('"')
        except KeyboardInterrupt: exit('Abort!')
        if len(path) < 1: continue
        if exists(path):
            if isfile(path): return(abspath(path))
            else: print(f"'{path}' is not a file.")
        else: print(f"Couldn't file: {path}.")
        print("Try again!")


def dirpath():
    '''Asks for a directory path to the user then,
    Returns absolute path of the directory if the directory exists.'''
    from os.path import abspath, exists, isdir
    while True:
        try: path = input("\nEnter directory path: ").strip().strip("'").strip('"')
        except KeyboardInterrupt: exit('Abort!')
        if len(path) < 1: path = '.'
        if exists(path):
            if isdir(path): return(abspath(path))
            else: print(f"'{path}' is not a directory path.")
        else: print(f"Couldn't locate: {path}.")
        print("Try again!")


def main():
    from os.path import basename
    
    menu = {}
    menu[1] = 'Get file path'
    menu[2] = 'Get directory path'
    menu[3] = 'Exit'
    for k, v in menu.items(): print(f'{k} : {v}')
    while True:
        try: option = int(input(f"Choose: ").strip())
        except KeyboardInterrupt: exit('Abort!')
        except ValueError:
            print('\n# Invalid input!\n  Try again.\n')
            continue
        if option in [k for k in menu.keys()]: return option
        print(
            f'\n# Value out of range!\n  Choose one of {[k for k in menu.keys()]}.\n')
    choosen = main()
    if choosen == 1:
        path = filepath()
        print(f"\nFilepath: {path}\nFilename: {basename(path)}")
    elif choosen == 2:
        path = dirpath()
        print(f"\nDirectory path: {path}\nDirectory name: {basename(path)}")
    else: exit('Bye..')


if __name__ == "__main__": main()

# The end.
