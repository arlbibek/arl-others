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
    print(ignores)
    return files


if __name__ == '__main__':

    files = get_files(".")

    # for file in files:
    #     print(file)
