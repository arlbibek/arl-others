def timer(time, msg='Please wait'):
    '''Prints like clock ticking
    Eg. {msg} {time} sec..'''
    from time import sleep
    Tcount = time
    try:
        fill = len(str(Tcount))
        for i in range(1, time + 1):
            print(
                f"{msg} {str(Tcount).zfill(fill)}/{str(time).zfill(fill)} sec..", end='\r')
            sleep(1)
            Tcount -= 1
        print(f"{msg} {Tcount}/{time} sec..", end='\r')
        print()
    except KeyboardInterrupt: exit('\nAbort!')


if __name__ == '__main__':
    from os.path import basename as bn
    print(f'''{bn(__file__)}
"""Prints like clock ticking"""
''')
    try:
        timer(int(input('Insert time in seconds.\n: ')), 'Timer:')
        print('[ Done ] Bye..')
    except Exception as e: exit(e)
    except KeyboardInterrupt: exit('Abort!')
