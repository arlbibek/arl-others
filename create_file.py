from datetime import datetime


def create_file(gb):
    gb *= 1024
    now = str(datetime.now()).replace(":", ".")

    filename = f'{str(gb/1024)} GB {now}'

    with open(filename, "w") as fh:
        fh.seek((1024 * 1024 * gb) - 1)
        fh.write('\0')
    print(f"[ done ] file created '{filename}'")


def get_size():
    while True:
        try:
            return float(input('Enter file size in GB: '))
        except ValueError:
            print('\nEnter an integer value.')
        except KeyboardInterrupt:
            exit('\n[ Keyboard Interrupt ] Abort!')


if __name__ == "__main__":
    print('CAUTION! '*3)
    file_size = get_size()
    create_file(file_size)
