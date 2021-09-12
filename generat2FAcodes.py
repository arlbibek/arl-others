print(f"""{__file__}

'''Generate 6 digit Two Factor authentication Codes'''

The generated codes will be written into a text file.
""")


def generate(fname):
    """writes 6 digit Two Factor authentication codes to 'fname'"""
    with open(fname, 'wt') as fa:
        print('Just a sec..')
        for n in range(100000, 1000000):
            try:
                fa.write(str(n) + '\n')
            except KeyboardInterrupt:
                continue


filename = '2FA_code.txt'
generate(filename)

exit(f"[ Done ] Results has been written to the text file named '{filename}'.")
# The End.
