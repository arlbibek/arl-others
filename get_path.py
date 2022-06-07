from ast import Return


def get_filepath(msg="Enter file path: "):
    '''Asks for a file path to the user then,
    Returns absolute path of the file if the file exist.'''

    from os.path import abspath, exists, isfile

    while True:
        try:
            path = input(f"{msg}").strip().strip("'").strip('"')
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
        except KeyboardInterrupt:
            print(
                f"\n[ Keyboard Interrupt ] '{get_filepath.__name__}' function stopped.")
            return None


def get_dirpath(msg="Enter directory path: "):
    '''Asks for a directory path to the user then,
    Returns absolute path of the directory if the directory exists.'''

    from os.path import abspath, exists, isdir

    while True:
        try:
            path = input(f"{msg}").strip().strip("'").strip('"')
            if len(path) < 1:
                path = '.'
            if exists(path):
                if isdir(path):
                    return(abspath(path))
                else:
                    print(f"'{path}' is not a directory path.")
            else:
                print(f"Couldn't locate: {path}.")
            print("Try again!")
        except KeyboardInterrupt:
            print(
                f"\n[ Keyboard Interrupt ] '{get_dirpath.__name__}' function stopped.")
            return None


if __name__ == "__main__":
    filepath = get_filepath()
    dirpath = get_dirpath()
    print(f"Filepath: {filepath}")
    print(f"Dirpath: {dirpath}")
# The end.
