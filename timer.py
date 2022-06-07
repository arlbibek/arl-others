def timer(seconds, msg='Timer:'):
    '''Prints like clock ticking.
    Use optional argument `msg` to print message such as 'Please wait' '''
    from time import sleep

    time_count = seconds

    try:
        fill = len(str(time_count))
        for _ in range(1, seconds + 1):
            print(
                f"{msg} {str(time_count).zfill(fill)}/{str(seconds).zfill(fill)} sec..", end='\r')
            sleep(1)
            time_count -= 1
        print(f"{msg} {time_count}/{seconds} sec..", end='\r')
        print()
        print(f"[ done ] {seconds} sec completed!")
    except KeyboardInterrupt:
        print(
            f"\n[ Keyboard Interrupt ] '{timer.__name__}' function stopped.")


if __name__ == '__main__':
    from sys import argv

    while True:
        try:
            if len(argv) > 1:
                timer(int(argv[-1]), 'Timer:')
                break
            else:
                timer(int(input('Insert time in seconds\n: ')), 'Timer:')
                break
        except ValueError:
            print(f"\n[ Value Error ] Input should be an integer.")
        except KeyboardInterrupt:
            exit(f"\n[ Keyboard Interrupt ] Exited!")
