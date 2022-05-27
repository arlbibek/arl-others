# Rename all file on a folder to randomly generated 6 digit code.
from os import listdir, rename
from os.path import isfile, join, exists, basename, abspath, splitext
from sys import argv


def getrandnumof(n):
    '''Returns randomly generated number with length of n'''
    import random
    return str(random.randrange(int(f'1{"0" * (n-1)}'), int(f'1{"0" * n}')))


def getdirpath():
    '''Get path of a valid directory'''
    while True:
        try:
            path = input(
                f'\nEnter directory (path) [RETURN = current directroy; CTRL + C = exit]\n: ').strip()
            if len(path) < 1:
                path = "."
            if isfile(path):
                print(f"\n'{path}' is a file not a directory.")
                continue
            if exists(path) is False:
                print(f"\nPath '{path}' does not exists.")
                continue
            return abspath(path)
        except KeyboardInterrupt:
            exit('Abort!')


def info():
    '''Prints additional information'''
    print("""
# additional info.
> File matching the following patterns will not be affected.
- Files with the name length less then seven excluding file extension\n   (eg. boo.mp3, 348233.png)
- Files without extension
- Files with '.py' extension
- Files with '.ini' extension
- Files that starts with '.' extension (hidden files)""")


def main():
    '''Rename all file on a folder to randomly generated 6 digit code.
    Eg: __fjdsl7439fRHzzt77UUvfTRe7362.png ==> 544305.png'''

    # Arguments if any
    dirpath = argv[1].strip().strip('"').strip("'") if len(
        argv) > 1 and not isfile(argv[1]) and exists(argv[1]) else ''

    if not len(dirpath) < 1:
        dirpath = abspath(dirpath)
    else:
        dirpath = getdirpath()

    # all files on the provided directory path
    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

    print(f'''
    # Directory Info.
    Path  : {dirpath}
    Name  : {basename(dirpath)}
    Items : {
        len(files)}  # Not all files are affected, see additional info above.''')

    # Final confirmation
    try:
        input("\nPress [RETURN] to continue or [CTRL + C] to abort..")
    except KeyboardInterrupt:
        exit('\nAbort!')

    count = 0
    for file in files:
        name, ext = splitext(basename(file))

        # Skips
        if file.endswith('.py'):
            continue   # Python files
        if file.endswith('.ini'):
            continue  # Init files
        if file.startswith('.'):
            continue   # Hidden files
        if len(ext) < 1:
            continue   # Files without extension
        if len(name) < 7:
            continue   # Files with name of 6 (or less) characters

        # Renaming files
        while True:
            src = join(dirpath, file)
            newname = f'{getrandnumof(6)}{ext}'
            dst = join(dirpath, newname)
            if not exists(dst):
                break
        count += 1
        print(f"{newname} <== {file}")
        rename(src, dst)

    msg = 'Noting to rename.'
    if count != 0:
        print('^New Name      ^Original Name')
        msg = f'{count} files renamed.'

    print(f"\n[ Done ] {msg}")


# Pausing the program at the end
if __name__ == '__main__':
    print(f"Rename all file on a folder to randomly generated 6 digit code.\nEg: __fjdsl7439fRHzzt77UUvfTRe7362.png ==> 544305.png")
    # additional info.
    info()
    while True:
        main()


# The End.
