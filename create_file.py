def createfile(gb):
    gb *= 1024
    with open(f'{str(gb/1024)}GiB', "w") as fh:
            fh.seek((1024 * 1024 * gb) - 1)
            fh.write('\0')

def getsize():
    while True:
        try: return int(input('Enter file size in GiB: '))
        except ValueError: print('\nEnter an interger value.')
        except KeyboardInterrupt: exit('Abort!')

print('CAUTION! '*3)
createfile(getsize())
