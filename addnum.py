print(f"""{__file__}

'''Add an auto increment numbers on each lines of a text file.'''

From:
    This is line one
    This a second line
    3. I'm line three
    Yay Fourth
To:
    1. This is line one
    2. This a second line
    3. I'm line three
    4. Yay Fourth
""")


def addnum():
    '''Add auto increment numbers on each lines of a text file'''
    while True:
        try:
            try: file = input('Enter filename (path): ')
            except KeyboardInterrupt: exit('Abort!')
            with open(file, 'rt', encoding="utf8") as fh:
                print(
                    f"A sequence of numbers 1. 2. 3. ... will be added to each line of the file '{file}'")
                try: input('Press [RETURN] to continue..')
                except KeyboardInterrupt: exit('Abort!')
                num = 0
                lines = fh.readlines()
                for line in lines:
                    num_fill = str(num + 1).zfill(len(str(len(lines))))
                    if not line.startswith(num_fill):
                        lines[lines.index(line)] = num_fill + '. ' + line
                    num += 1
                break
        except FileNotFoundError: print(f'Could not locate, {file}\nTry again..')
    with open(file, 'wt', encoding="utf8") as fh:
        for line in lines:
            fh.write(line)
    print('Lines: ', num)
    if num < 1: print('Noting to write!')
    else: print(f"'{file}' updated!")


if __name__ = "__main__":
    addnum()
    print("\n[ Done ]")
    exit('\nBye..')

# The End.
