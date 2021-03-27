def timer(time, msg=''):
    '''Prints like clock ticking'''
    from time import sleep
    time_count = time
    try:
        fill = len(str(time_count))
        for _ in range(1, time + 1):
            print(
                f"{msg} {str(time_count).zfill(fill)}/{str(time).zfill(fill)} sec..", end='\r')
            sleep(1)
            time_count -= 1
        print(f"{msg} {time_count}/{time} sec..", end='\r')
        print()
    except KeyboardInterrupt as e:
        print(e)


if __name__ == '__main__':
    from sys import argv
    print(f"\n\t'''Prints like clock ticking'''\n")
    while True:
        if len(argv) > 1:
            try:
                timer(int(argv[-1]), 'Timer:')
                print('[ Done ] ')
                break
            except ValueError as e:
                pass
        try:
            timer(int(input('Insert time in seconds\n: ')), 'Timer:')
            print('[ Done ] ')
            break
        except ValueError as e:
            break
        except KeyboardInterrupt:
            break
