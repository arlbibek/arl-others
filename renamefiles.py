# Rename all file on a folder to randomly generated 6 digit code.
from os import listdir, rename
from os.path import isfile, join, exists, basename, abspath
from sys import argv
print(f"""
FILE: {basename(__file__)}

Rename all file on a folder to randomly generated 6 digit code.
    Eg: __fjdsl7439fRHzzt77UUvfTRe7362.png ==> 544305.png""")

# Aruments if any
dirpath = argv[1].strip().strip('"').strip("'") if len(argv) > 1 and not isfile(argv[1]) and exists(argv[1]) else ''


def get_name_ext(fpath):
    '''Returns name, extension from a file name'''
    fname = basename(fpath)
    split = fname.split('.')
    if len(split) < 2: return fname, None
    ext = split[-1]
    del split[-1]
    fname = '.'.join([i for i in split])
    return fname, ext


def getrand6():
    '''Returns randomly generated 6 digit number'''
    import random
    return str(random.randrange(100000, 1000000))


def getdirpath():
    '''Get path of a valid directory'''
    while True:
        try:
            path = input('\nEnter directory (path)\n: ').strip()
            if len(path) < 1: path = "."
            if isfile(path):
                print(f"\n'{path}' is a file not a directory.")
                continue
            if exists(path) is False:
                print(f"\nPath '{path}' does not exists.")
                continue
            return abspath(path)
        except KeyboardInterrupt: exit('Abort!')


def info():
    '''Prints addtional information'''
    print("""
# Addtional info.
> File matching the following patterns will not be affected.
- Files with the name length less then seven excluding file extension\n   (eg. boo.mp3, 348233.png)
- Files without extension
- Files with '.py' extension
- Files with '.ini' extension
- Files that starts with '.' extension (hidden files)""")


if not len(dirpath) < 1: dirpath = abspath(dirpath)
else: dirpath = getdirpath()

# all files on the provided directory path
files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

# Addtional info.
info()

print(f'''
# Directory Info.
  Path  : {dirpath}
  Name  : {basename(dirpath)}
  Items : {len(files)}  # Not all files are affected, see Addtional Info above.''')

# Final confirmation
try: input("\nPress [RETURN] to continue or [CTRL + C] to abort..")
except KeyboardInterrupt: exit('\nAbort!')

count = 0
for file in files:
    name, ext = get_name_ext(abspath(file))

    # Skips
    if file.endswith('.py'): continue   # Python files
    if file.endswith('.ini'): continue  # Init files
    if file.startswith('.'): continue   # Hidden files
    if ext is None: continue            # Files without extension
    if len(name) < 7: continue          # Files with name of 6 (or less) characters

    # Renaming files
    while True:
        src = join(dirpath, file)
        newname = f'{getrand6()}.{ext}'
        dst = join(dirpath, newname)
        if not exists(dst): break
    count += 1
    print(f"{newname} <== {file}")
    rename(src, dst)

msg = 'Noting to rename.'
if count != 0:
    print('^New Name      ^Original Name')
    msg = f'{count} files renamed.'

print(f"\n[ Done ] {msg}")

# Pausing the porgram at the end
if __name__ == '__main__': input()

# The End.
