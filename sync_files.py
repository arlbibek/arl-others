def getdirpath(txt):
    '''Asks for a directory path to the user then,
    Returns absolute path of the directory if the directory exists.'''
    from os.path import abspath, exists, isdir
    while True:
        try:
            path = input(f"{txt}").strip().strip(
                "'").strip('"')
        except KeyboardInterrupt:
            exit('Abort!')
        if len(path) < 1:
            path = '.'
        if exists(path):
            if isdir(path):
                return(abspath(path))
            else:
                print(f"'{path}' is not a directory path.")
        else:
            print(f"Couldn't locate directory: '{path}'")
        print("Try again!")


def getfiles(path):
    '''Returns a list of files in the given directory path (including files in subdirectories)'''
    from os import walk
    from os.path import join,  isfile

    all_files = []
    for dirpath, dirnames, filenames in walk(path, topdown=False):
        for name in filenames:
            filepath = join(dirpath, name)
            if isfile(filepath):
                all_files.append(filepath)
        for name in dirnames:
            filepath = join(dirpath, name)
            if isfile(filepath):
                all_files.append(filepath)
    return all_files


def main(srcpath, distpath, ignore=()):
    '''Sync directories
    Copy all files from a directory tree (i.e. {srcpath}) to 
    a single directory (i.e. {distpath})
    use {ignore} to ignore certain type of files e.g. ignore = (".txt",".py")'''
    from os.path import basename
    from shutil import copy

    sourcefiles = getfiles(srcpath)
    distfilesnames = [basename(f) for f in getfiles(distpath)]

    print(f"""
Source: {srcpath}
Destination: {distpath}
""")

    count = 0
    for filepath in sourcefiles:
        if filepath.endswith(ignore):
            continue
        if basename(filepath) in distfilesnames:
            continue
        print(f"Coping {filepath} ..", end="")
        copy(filepath, distpath)
        count += 1
        print(". done")
    print(f"[ done ] {count} files copied from to '{srcpath}'")


if __name__ == "__main__":
    while True:
        srcpath = getdirpath("Source directory: ")
        distpath = getdirpath("Destination directory: ")

        if srcpath == distpath:
            print("Please choose a different destination path! ")
            continue
        break

    main(srcpath, distpath)
