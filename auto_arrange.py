# auto arrange lines of a file in a Ascending or ddescending order
from sys import argv
desc = True if argv[-1] == '-d' else False
pyfile = __file__.split('\\')[-1]

order = 'Descending' if desc else 'Ascending'
if not desc: print(
    f"USE ARGUMENT:\n-d \t- to sort contents in Descending order.\n\t  Eg.{pyfile} -d")


def sort_lines():
    while True:
        try:
            filename = input(
                f"Enter name of the file to sort in {order} order: ")
            lines = open(filename, 'rt')
            break
        except FileNotFoundError:
            print(f"Error: Couldn't locate {filename}")
            continue
        except KeyboardInterrupt: exit("Abort!")
    next(lines)  # Skip first line
    lines = [line.strip() for line in lines]
    lines.sort(reverse=desc)

    # Writhing new sorted items
    with open('sorted_' + filename, 'wt') as sor:
        for line in lines:
            sor.write(f'{line}\n')
    print(
        f'\nContents of the the file {filename} has been sorted in {order} order.')
    print(f'Check sorted_{filename}')
    exit('Bye..')


sort_lines()
