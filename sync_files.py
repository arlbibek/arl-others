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


def get_files(path, ignore=[]):
    '''Takes directory path and returns a list containing path of all files in that directory
    (including the files in subdirectories)'''
    # REFERENCES: https://stackoverflow.com/questions/120656/directory-tree-listing-in-python

    from os import walk
    from os.path import join, abspath

    files = []

    for dirname, dirnames, filenames in walk(path):
        # path to all filenames.
        for filename in filenames:
            files.append(abspath(join(dirname, filename)))

        # ignore directories.
        ignores = ['.git', '__pycache__', ".vscode", "node_modules"] + ignore

        for i in ignores:
            if i in dirnames:
                dirnames.remove(i)
    return files


def sync_files(src_path, dist_path, ignore_files=()):
    '''Sync directories
    Copy all files from a directory tree (i.e. {src_path}) to 
    a single directory (i.e. {dist_path})
    use {ignore_files} to ignore certain type of files e.g. ignore_files = (".txt",".py")'''

    from os.path import basename
    from shutil import copy

    source_files = get_files(src_path)
    dist_file_names = [basename(f) for f in get_files(dist_path)]

    print(f"""
Source: {src_path}
Destination: {dist_path}
""")

    count = 0
    for filepath in source_files:
        if filepath.endswith(ignore_files):
            continue
        if basename(filepath) in dist_file_names:
            continue
        print(f"Coping {filepath} ..", end="")
        copy(filepath, dist_path)
        count += 1
        print(". done")
    print(f"[ done ] {count} files copied from to '{src_path}'")


if __name__ == "__main__":
    while True:
        src_path = get_dirpath("Source directory: ")
        dist_path = get_dirpath("Destination directory: ")

        if src_path == None or dist_path == None:
            exit(f"\nSource path or destination path can't be 'None'. \nExiting..")
        if src_path == dist_path:
            print("\nPlease choose a different destination path!")
            continue

        break
    sync_files(src_path, dist_path)
