def getyesno(question='Continue'):
    """Returns 'True' if input is 'yes', 'False' if 'no'"""
    if not question.endswith('?'): question += '?'
    while True:
        try:
            ans = input(f'{question} [Y/n] ').lower().strip()
            if ans in ['y', 'yes']: return True
            elif ans in ['n', 'no']: return False
        except: pass

if __name__ == "__main__":
    print('Have a nice day!' if getyesno(
        "Is the sky blue?") else 'Grass is always greener on the other side.')
    input('Bye..')
    exit()

    # The End.