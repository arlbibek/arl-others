# Generet 6 digit Two Factor Authencatation Codes
def get_2fa_fastter():
    """Generating 6 digit Two Factor Authencatiion Codes"""
    with open('2FA_code.txt', 'wt') as fa:
        for n in range(100000, 1000000):
            try:
                fa.write(str(n) + '\n')
            except KeyboardInterrupt:
                continue
            except Exception as e:
                raise e
        exit()


get_2fa_fastter()
