def fget(msg=''):
    '''Return filename, filepath from an given input'''
    from os.path import exists, isfile, abspath, basename

    while True:
        try:
            filepath = input(
                f"Enter filename (or path) {msg}\n: ").strip().strip('"').strip("'").strip()
            filepath = abspath(filepath)
            filename = basename(filepath)
            print()
            if not exists(filepath):
                print(f"Couldn't locate: {filename}")
                continue
            if not isfile(filepath):
                print(f"We need a filename (path) not a directory name.")
                continue
            return filename, filepath
        except KeyboardInterrupt: exit("Abort!")


if __name__ == "__main__":
    fname, fpath = fget()
    print(f"\nFilepath: {fpath}\nFilename: {fname}")
