# Rename all file on a folder to randomly generated 6 digit code.

from os import listdir, rename
from os.path import isfile, join, exists

print(f"""{__file__}
Rename all file on a folder to randomly generated 6 digit code.
    Eg: __fjdsl7439fRHzzt77UUvfTRe7362.png ==> 544305.png
""")


def get_name_ext(full_name):
    '''Returns name, extension from a file name'''
    split = full_name.split('.')
    if len(split) < 2: return full_name, None
    ext = split[-1]
    del split[-1]
    name = '.'.join([i for i in split])
    return name, ext


def getrand6():
    '''Returns randomly generated 6 digit number'''
    import random
    return str(random.randrange(100000, 1000000))


while True:
    while True:
        try:
            mypath = input('Enter directory (path)\n: ').strip()
            if len(mypath) < 1: continue
        except KeyboardInterrupt: exit('Abort!')
        if isfile(mypath):
            print('\nIs it a file. We need directory (path).')
            continue
        if exists(mypath) is False:
            print(f"\nPath '{mypath} does not exists.'\nTry again!")
            continue
        break
    # Listing the contains
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if len(files) > 0: break
    else: print("The directory doesn't seem to have any files.\nTry again with different directory (path)\n")

# Setting file count limit
if len(files) > 900_000:
    print(
        "Sorry! :(\nI'm not designed to rename more than 900,000 files at a time.")
    exit(f"The directory has {len(files)}.\nBye..")

print(f"{len(files)} file(s) found on '{mypath}'")
# print([f for f in files])  # print all file name as a as a list
print()
print('Note: File matching the following patterns will not be affected.')
print(' - Files with the name length less then seven excluding file extension\n   (eg. boo.mp3, 348233.png)')
print(' - Files without extension')
print(" - Files with '.py' extension")
print(" - Files with '.ini' extension")
print(" - Files that starts with '.' extension (hidden files)")


# Final confirmation
try: input("\nPress [RETURN] to continue or [CTRL + C] to abort..\n")
except KeyboardInterrupt: exit('Abort!')

count = 0
for file in files:
    nameandext = get_name_ext(file)
    name = nameandext[0]
    ext = nameandext[-1]

    # Skips
    if file.endswith('.py'): continue  # python files
    if file.endswith('.ini'): continue
    if file.startswith('.'): continue
    if ext is None: continue  # files without extension
    # files with name less than six letters (or numbers)
    if len(name) < 7: continue

    # Renaming files
    while True:
        src = f'{mypath}\\{file}'
        newname = f'{getrand6()}.{ext}'
        dst = f'{mypath}\\{newname}'
        if exists(dst) is True: print(
            f'File "{newname}" already exists.Trying again!.')
        else: break
    count += 1
    print(f'{newname} <== {file}')
    rename(src, dst)
msg = 'Noting to rename.'
if count != 0:
    print('^New Name      ^Original Name')
    msg = f'{count} files renamed.'

print(f"\n[ Done ] {msg}\nBye..")
input('Enter [RETURN] to exit..')
exit()
# The End.
