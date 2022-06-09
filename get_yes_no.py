def get_yes_no(question='Continue', error=False):
    """Returns 'True' if input is 'yes', 'False' if 'no'
    Set error=True to return 'None' on Keyboard interruption, other wise ask till you get either 'Yes' or 'No'"""
    if not question.endswith('?'):
        question += '?'
    while True:
        try:
            ans = input(f'{question} [Y/n] ').lower().strip()
            if ans in ['y', 'yes']:
                return True
            elif ans in ['n', 'no']:
                return False
        except KeyboardInterrupt:
            if error:
                print("[ Keyboard INterrupt ]")
                return None
            else:
                print()
                continue


if __name__ == "__main__":
    print('Have a nice day!' if get_yes_no(
        "Is the sky blue?", False) else 'Grass is always greener on the other side.')
