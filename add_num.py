from get_path import get_filepath


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

            # adding the auto increment numbers before each lines of the text file
            with open(file, 'wt', encoding="utf8") as fh:
                for line in lines:
                    fh.write(line)
            print(
                f"[ done ] {basename(file)} file updated! (Changed {change_count} {'lines' if change_count > 1 else 'line'})")
        except KeyboardInterrupt:
            print(
                f"\n[ Keyboard Interrupt ] '{add_num.__name__}' function stopped.")

    else:
        print(f"Noting to write on the file '{basename(file)}'")


if __name__ == "__main__":
    file = get_filepath()
    if file is None:
        print(f"Got '{file}' from the user. Exiting...")
    else:
        add_num(file)

# Made with ❤️ by Bibek Aryal.
