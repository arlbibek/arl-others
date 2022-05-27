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


def confirm(msg):
    '''Get confirmation from the user with "Press [RETURN] to continue.."'''
    print(msg)
    try:
        input('Press [RETURN] to continue..')
        return True
    except KeyboardInterrupt:
        return False


def addnum():
    '''Add auto increment numbers on each lines of a text file'''
    from os.path import basename

    file = getfilepath()

    lines_count = 0
    changes_count = 0

    with open(file, 'rt', encoding="utf8") as fh:
        lines = fh.readlines()
        len_lines = len(lines)
        len_fill = len(str(len_lines))

        print("Reading file..")
        for line in lines:
            num_fill = str(lines_count + 1).zfill(len_fill)
            if not line.startswith(num_fill):
                lines[lines.index(line)] = f"{num_fill}. {line}"
                changes_count += 1
            lines_count += 1

    print(f"""
# File details

  File Path: {file}
  File Name: {basename(file)}
  Total Lines: {lines_count}
""")
    if not changes_count < 1 or not lines_count < 1:
        # Confirmation
        if not confirm(f"A sequence of numbers (1., 2., 3., and so on) will be added to each line of the file"):
            exit("Abort!")
        print()

        # MAIN: adding the auto increment numbers before each lines of the text file
        with open(file, 'wt', encoding="utf8") as fh:
            for line in lines:
                fh.write(line)
        return f"'{basename(file)}' file updated! [Changed '{changes_count}' line(s).]"
    return "Noting to write!"


if __name__ == "__main__":
    print(f"[ done ] {addnum()}")
    try:
        from time import sleep
        print("Ending..")
        sleep(2)
    except Exception:
        pass


# The End.
