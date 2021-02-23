def ynq(question='Continue'):
    """Returns 'True' if input is 'yes', 'False' if 'no'"""
    print()
    if not question.endswith('?'): question += '?'
    while True:
        try:
            ans = input(f'{question} [Y/n] ').lower().strip()
            if ans in ['y', 'yes']: return True
            elif ans in ['n', 'no']: return False
        except: print()


if __name__ == "__main__":
    print(f"""{__file__}
    '''a simple yes or no question'''
    """)
    print('Have a nice day!' if ynq(
        "Is the sky blue?") else 'Grass is always greener on the other side man.')
    exit('Bye..')

    # The End.