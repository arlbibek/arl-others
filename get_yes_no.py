def ynq(question=None):
    """Get True or False from User"""
    while True:
        print(question)
        try:
            ans = input('(y/n)[RETURN = y]: ').lower().strip(' ')
        except KeyboardInterrupt:
            exit('\nAbort!')
        if ans in ['y', 'yes'] or len(ans) < 1:
            return True
        elif ans in ['n', 'no']:
            return False
        print("Invalid Input!!\nEnter 'y' for 'Yes' or 'n' for 'No'")
        continue


if ynq('Is the sky blue?'):
    print('Have a nice day!')
    exit('Bye..')
exit('Bye..')
