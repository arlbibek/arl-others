def addnum(file=str()):
    '''Add auto increment numbers on each lines of a text file'''
    while True:
        try:
            with open(file, 'rt', encoding="utf8") as fh:
                num = 1
                lines = fh.readlines()
                for line in lines:
                    num_fill = str(num).zfill(len(str(len(lines))))
                    if not line.startswith(num_fill):
                        lines[lines.index(line)] = num_fill + '. ' + line
                    num += 1
                break
        except FileNotFoundError:
            try: file = input('Enter filename: ')
            except KeyboardInterrupt: exit('Abort!')
    with open(file, 'wt', encoding="utf8") as fh:
        for line in lines:
            fh.write(line)
    print('Lines: ', num)


addnum()
