def getfiles(path):
    from os import walk
    from os.path import join,  isfile

    all_files = []
    '''Returns a list of all files in the given directory path (including files in subdirectories)'''
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
    '''Sync music folders'''
    from os.path import basename
    from shutil import copy

    sourcefiles = getfiles(srcpath)
    distfilesnames = [basename(f) for f in getfiles(distpath)]

    print(f"""
Source Path: {srcpath}
Destination Path: {distpath}
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
    print(f"[ Done ] {count} files copied from '{distpath}'")


if __name__ == "__main__":
    srcpath = input("Source directory: ")
    distpath = input("Distnation directory: ")

    main(srcpath, distpath)

    input("\nHit [RETURN] to exit..")
