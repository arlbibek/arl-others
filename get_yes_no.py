def ynq(question=None):
    """Get True or False from User"""
    while True:
        print(question)
        try:
            ans = input('(y/n)[RETURN = y]: ')
        except KeyboardInterrupt:
            exit('\nAbort!')
        if ans in ['y', 'Y', 'yes', 'Yes', 'YES'] or len(ans) < 1:
            return True
        elif ans in ['n', 'N', 'no', 'No', 'NO']:
            return False
        print("Invalid Input!!\nEnter 'y' for 'Yes' or 'n' for 'No'")
        continue


print(ynq('Is the sky blue?'))
