def ask(msg="", ask=True):
    '''Returns 'True' if userinput in 'RETURN' or 'False' otherwise.'''
    if not ask: return True
    print()
    print(msg)
    try:
        input('Press [RETURN] to continue or [CTRL + C] to abort..')
        return True
    except KeyboardInterrupt: return False
    except Exception: return False


def rmdublicatelines(filepath, confirm=True):
    '''Remove duplicate lines from a (text) file.'''
    from os.path import basename, abspath
    from collections import OrderedDict

    filepath = abspath(filepath)
    lines = list(open(filepath, 'rb'))
    uniquelines = list(OrderedDict.fromkeys(lines))

    lcount = len(lines)  # total line on the original file
    uqlcount = len(uniquelines)  # total unique lines

    if lcount == uqlcount: print('No duplicate lines to remove.')
    else:
        msg = f"The file '{basename(filepath)}' is to be modified. Are you sure?"
        if not ask(msg, confirm): print('Abort!\n\n[ Aborted ] No changes.')
        else:
            # Writing the unique lines to the file
            open(filepath, "w")     # Clearing the original file
            with open(filepath, 'ab') as fh:
                for line in uniquelines: fh.write(line)
            # Displaying details to user
            print(
                f'\n[ Done ] Removed {lcount - uqlcount} duplicate lines out of {lcount}.')


def rmlessthan(n, filepath, confirm=True):
    '''Remove lines with less thatn certain (n) numbers charecters from a file.'''
    from os.path import basename, abspath

    filepath = abspath(filepath)
    lines = list(open(filepath, 'rb'))
    validlines = []

    for line in lines:
        if not len(line.decode(errors='ignore').strip()) < n:
            validlines.append(line)

    lcount = len(lines)  # total lines from original file
    vlclount = len(validlines)  # total valid lines
    rml = lcount - vlclount  # total lines removed

    if lcount == vlclount: print('Noting to remove.')
    else:
        # Confirmation then execution
        msg = f"The file '{basename(filepath)}' is to be modified. Are you sure?"
        if not ask(msg, confirm): print('Abort!\n\n[ Aborted ] No changes.')
        else:
            # Writing the valid lines to the file
            open(filepath, "w")  # Clearing the original file
            with open(filepath, 'ab') as fh:
                for line in validlines: fh.write(line)
            # Displaying details to user
            print(
                f"\n[ Done ] Removed {rml} lines out of {lcount} from the file '{basename(filepath)}'.")


def getpath():
    '''Returns a valid file path from the user input.'''
    from os.path import abspath, exists, isfile
    while True:
        try:
            path = abspath(
                input('Enter filepath: ').strip().strip('"').strip("'"))
            if exists(path) and isfile(path): return path
            print("\nInvalid path: Enter a file path!\n")
        except KeyboardInterrupt: exit('Abort!\nBye..')


def main():
    '''Main'''
    menu = {}
    menu[1] = "Remove duplicate lines from a (text) file"
    menu[2] = "Remove lines with less thatn certain (n) numbers charecters from a file."

    for k, v in menu.items(): print(k, v)
    while True:
        try:
            option = int(input('Choose: '))
            if option in [k for k in menu.keys()]: break
            print(f'Invalid input: choose one from {[k for k in menu.keys()]}')
        except ValueError: continue
        except KeyboardInterrupt: exit('Abort!')
    if option == 1: rmdublicatelines(getpath())
    else: rmlessthan(int(input("Less then?: ")), getpath())


if __name__ == "__main__": main()
