def ynq(question=""):
    """Get True or False from User"""
    while True:
        try:
            ans = input(str(question) + '(y/n): ').lower().strip(' ')
        except KeyboardInterrupt:
            exit('Abort!')
        if ans in ['y', 'yes', 'true'] or len(ans) < 1:
            print("Yes")
            return True
        elif ans in ['n', 'no', 'false']:
            print("No")
            return False
        print("Invalid Input!!\nEnter 'y' for 'Yes' or 'n' for 'No'")
        continue


if ynq():
    print('Have a nice day!')
exit('Bye..')
