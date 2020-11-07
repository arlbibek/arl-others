print("""Name: autorenamefiles.py

'''Rename all file on a folder to randomly generated 6 digit code.'''

From:
    filename: __fjdsl7439fRHzzt77UUvfTRe7362.png
To
    filename: 544305.png

Requirements: None
""")


from os import listdir, rename
from os.path import isfile, join, exists, isdir, isfile


def getrandnum():
    '''Returns randomly generated 6 digit number'''
    import random
    return random.randrange(99_999, 1_000_000)


while True:
    while True:
        try: mypath = input('Enter directory (path)\n: ')
        except KeyboardInterrupt: exit('Abort!')
        if isfile(mypath):
            print('\nIs it a file. We need directory. (path)')
            continue
        if exists(mypath) is True: break
        print(f"\nCould not locate: '{mypath}'\n\nTry again!")
        continue

    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if len(files) > 1: break
    print("The directory doesn't seem to have any files.")

# Setting file limit
if len(files) > 900_000:
    print(
        "Sorry! :(\nI'm not designed to rename more than 900,000 files at a time.")
    exit(f"The directory has {len(files)}.\nBye..")

fcount = len(files) - 1  # Number of file on the given directory
print(f"\n{fcount} files found on '{mypath}'\n")

# Getting final confirmation
try: input("Press [RETURN] to continue..")
except KeyboardInterrupt: exit('Abort!')
except Exception: exit("Something is not right. Abort!")

for file in files:
    # TO DO: Check and skip if the file already has appropriate name

    # Skipping if file does not have an extension
    if len(file.split('.')) < 2: continue

    # Extracting file extension
    file_ext = file.split('.')[-1]

    # Renaming files
    while True:
        src = f'{mypath}\\{file}'
        new_fname = f'{getrandnum()}.{file_ext}'
        dst = f'{mypath}\\{new_fname}'
        if exists(dst) is False: break
        print(f'File "{new_fname}" already exists. Getting another name.')
    rename(src, dst)

print("\n[ Done ] All files renamed.")
exit('\nBye..')

# The End.
