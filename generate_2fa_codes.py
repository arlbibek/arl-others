
def generate(filename="2FA_code.txt", display=False):
    """Writes 6 digit Two Factor authentication codes to 'filename'
    Set  display=True to print the codes as well."""
    with open(filename, 'wt') as fa:
        for n in range(100000, 1000000):
            try:
                fa.write(str(n) + '\n')
                if display:
                    print(n)
            except KeyboardInterrupt:
                print("[ Keyboard Interrupt ]")
                return None
        print(
            f"[ Done ] Results has been written to the text file named '{filename}'.")


if __name__ == "__main__":
    generate(display=True)
