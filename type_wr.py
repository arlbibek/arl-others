def type_wr(string, speed=0.05):
    """Prints string in a type writer effect.
    `speed`: Set the speed of the type writing effect in seconds (default is 0.05s), this may be a floating point number for subsecond precision.
    """
    from time import sleep
    import sys

    speed = float(speed)
    stopple_char = ['!', ',', '.', ':', ';', '?']
    try:
        for letter in string:
            sleep(speed)
            sys.stdout.write(letter)
            sys.stdout.flush()

            stop_time = speed * 2
            if letter in ["."]:
                sleep(1) if stop_time < 1 else sleep(stop_time)
            elif letter in stopple_char:
                sleep(stop_time)
        print()
    except KeyboardInterrupt:
        print(
            f"\n[ Keyboard Interrupt ] '{type_wr.__name__}' function stopped.")


if __name__ == "__main__":
    type_wr("""Hello, World!
Today, Let me tell you a little bit about Planktons.
Plankton are the diverse collection of organisms found in water that are unable to propel themselves against a current. The individual organisms constituting plankton are called plankters. In the ocean, they provide a crucial source of food to many small and large aquatic organisms, such as bivalves, fish and whales. """)
