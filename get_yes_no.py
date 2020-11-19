print("""Name: get_yes_no,py

'''Simple yes or no question'''
""")


def get_Yn(question=""):
    """Returns 'True' if input is 'yes', 'False' if 'no'"""
    while True:
        try: ans = input(str(question) + ' [Y/n] ').lower().strip(' ')
        except KeyboardInterrupt: exit('Abort!')
        if ans in ['y', 'yes', 'true'] or len(ans) < 1: return True
        elif ans in ['n', 'no', 'false']: return False
        print("Invalid Input!!\nEnter 'y' for 'Yes' or 'n' for 'No'")


if get_Yn("Is the sky blue?"): print('Have a nice day!')
else: print("Grass is always greener on the other side man.")

exit('Bye..')

# The End.
