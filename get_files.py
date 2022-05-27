def getfiles(path):
    '''Takes directory path and returns a list containing path of all files in that directory
    (including the files in subdirectories)'''

    from os import walk
    from os.path import join, abspath

    allfiles = []

    # REFERENCES:
    # > https://stackoverflow.com/questions/120656/directory-tree-listing-in-python
    for dirname, dirnames, filenames in walk(path):
        # path to all filenames.
        for filename in filenames:
            allfiles.append(abspath(join(dirname, filename)))

        # ignore directories.
        ignore = ['.git', '__pycache__']
        for i in ignore:
            if i in dirnames:
                dirnames.remove(i)

    return(allfiles)


if __name__ == '__main__':
    def getpath():
        from os.path import abspath, exists, isdir
        '''Returns directory path provide by the user'''
        while True:
            try:
                path = input("\nEnter directory path: ").strip()
            except KeyboardInterrupt:
                exit('\nAbort!')
            if len(path) < 1:
                path = "."
            if exists(path):
                if isdir(path):
                    return(abspath(path))
                else:
                    print(f"'{path}' is not a directory path.")
            else:
                print(f"Couldn't locate: {path}.")
            print("Try again!")

    # printing list of files
    for file in getfiles(getpath()):
        print(file)
