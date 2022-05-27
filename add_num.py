def get_input(msg="Enter", num=False):
    """Return a valid input from the user.

    Use `msg="Your text here"` to display the input prompt to the user.

    Use `num=True` parameter for a valid integer input. Please note that the input must be greater than 0.

    Also, Entering `.exit` in the prompt will terminate the program in any given time.
    """

    while True:
        try:
            user_input = input(f"{msg}: ").strip()
            if user_input == ".exit":
                exit("[ OK ] Exiting...")

            if len(user_input) < 1:
                print("[ Invalid input ] Please do not leave the fields empty..")
                continue
            if num:
                try:
                    user_input = int(user_input)

                    # 'user_input' is to be greater than '0'
                    if user_input > 1:
                        print(
                            f"[ Invalid input '{user_input}'] Added value must be greater than '0'. Please try again!")
                        continue

                except ValueError:
                    print(
                        f"[ Invalid input ] Entered value must be an integer.")
                    continue
            return user_input
        except KeyboardInterrupt:
            exit("\n[ Keyboard Interrupt ] Exiting...")


def get_filepath():
    '''Returns absolute path of the file if the file exist.'''
    from os.path import abspath, exists, isfile
    while True:
        path = get_input("Enter filepath")
        if exists(path):
            if isfile(path):
                return(abspath(path))
            else:
                print(f"[ error ] '{path}' is not a file.")
        else:
            print(f"[ error ] Couldn't locate file on: {path}")

        print("Try again!")


def confirm(msg=""):
    '''Get confirmation from the user with "Press [RETURN] to continue.."'''
    print(msg)
    try:
        input('Press [RETURN] to continue.')
        return True
    except KeyboardInterrupt:
        return False


def add_num(file):
    """Adds an auto increment numbers on each lines of a file.

    Eg.

    ```text
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
    ```"""

    from os.path import basename

    lines_count = 0
    change_count = 0

    print("Reading file..")
    with open(file, 'rt', encoding="utf8") as fh:
        lines = fh.readlines()
        len_lines = len(lines)
        len_fill = len(str(len_lines))

        for line in lines:
            num_fill = str(lines_count + 1).zfill(len_fill)
            if not line.startswith(num_fill):
                lines[lines.index(line)] = f"{num_fill}. {line}"
                change_count += 1
            lines_count += 1

    print(f"""
# File details

  File path: {file}
  File name: {basename(file)}
  Total lines: {lines_count}
""")

    if not change_count < 1 or not lines_count < 1:

        # confirmation
        try:
            print(
                f"A sequence of numbers (1., 2., 3., and so on) will be added to each line of the file '{basename(file)}'")
            input('Press [RETURN] to continue')
        except KeyboardInterrupt:
            exit("\n[ abort ] Exiting..")

        # adding the auto increment numbers before each lines of the text file
        with open(file, 'wt', encoding="utf8") as fh:
            for line in lines:
                fh.write(line)
        print(
            f"[ done ] {basename(file)} file updated! (Changed {change_count} {'lines' if change_count > 1 else 'line'})")
    else:
        print(f"Noting to write on the file '{basename(file)}'")


if __name__ == "__main__":
    file = get_filepath()
    add_num(file)

# Made with ❤️ by Bibek Aryal.
