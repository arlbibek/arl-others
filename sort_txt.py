from sys import argv
from os.path import exists, isfile, abspath, dirname
print(f"""{__file__}

'''Sort contents of a text file into ascending or descending order'''

From:
    38501000, Poland
    76355000, Iran
    112336538, Mexico
    33330000, Iraq
To:
    112336538, Mexico
    33330000, Iraq
    38501000, Poland
    76355000, Iran

USE: -d for descending

Requirements: None
""")

# USE:
# -d, -descending     to sort contents of the file in descending order.
#                     ascending by default if no arguments has been given.


desc = True if len(argv) > 1 and argv[1].lower() in [
    '-d', '-descending'] else False


def getfile():
    '''Return filename and it's full path from an given input'''
    while True:
        try:
            filepath = input(
                f"Enter filename or path of file to sort: ").strip().strip('"')
            filename = str()
            if ('\\') in filepath: filename = filepath.split('\\')[-1]
            else:
                filename = filepath
                filepath = f'{dirname(abspath(__file__))}\\{filename}'
            if exists(filepath):
                if isfile(filepath): return filename, filepath
                print(f'{filepath} is a directory!\nWe need a file.')
                continue
            print(f"Couldn't locate: {filename}.\nTry with another!!")
        except KeyboardInterrupt: exit("Abort!")


filename, filepath = getfile()

# Confirming when the provided file is not a .txt file
if not filename.endswith('.txt'):
    print(f"\nThe file '{filename}' is not a '.txt' file. Are you sure?")
    try: input('Press [RETURN] to continue or [CTRL + C] to abort..')
    except KeyboardInterrupt: exit('\nAbort!')


sort_order = 'descending' if desc is True else 'ascending'

print(f'''
File Path  : {filepath}
File Name  : {filename}
Sort Order : {sort_order.title()}
''')

with open(filepath, 'rt') as lines:
    sorted_lines = sorted([line.strip() for line in lines], reverse=desc)

# Confirmation
print(
    f"The file '{filename}' (original) will be modified (i.e. sorted in {sort_order}).")
try: input('Press [RETURN] to continue or [CTRL + C] to abort..')
except KeyboardInterrupt: exit('\nAbort!')

open(f'{filepath}', 'wt')  # Clearing the contents of the file

for line in sorted_lines:
    with open(f'{filepath}', 'at') as fh:
        fh.write(f'{line}\n')
exit(
    f"\n[ Done ] The contents of the file '{filename}' has been sorted to {'descending' if desc is True else 'ascending'} order.")
