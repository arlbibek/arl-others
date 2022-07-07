def get_input(msg="Enter", num=False):
    """Return a valid input from the user.

    Use `msg="Your text here"` to display the input prompt to the user.

    Use `num=True` parameter for a valid integer input. Please note that the input must be greater than 0.

    Also, Entering `.exit` in the prompt will terminate the program in any given time.
    """

    while True:
        try:
            user_input = input(f"{msg}: ").strip()

            if user_input == ".exit":
                exit("[ OK ] Aborted!")

            if len(user_input) < 1:
                print("[ Invalid input ] Please do not leave the fields empty..")
                continue
            if num:
                try:
                    user_input = int(user_input)

                    # 'user_input' is to be greater than '0'
                    if user_input < 1:
                        print(
                            f"[ Invalid input '{user_input}'] Added value must be greater than '0'. Please try again!")
                        continue

                except ValueError:
                    print(
                        f"[ Invalid input ] Entered value must be an integer.")
                    continue
            return user_input
        except KeyboardInterrupt:
            try:
                print("[ Keyboard Interrupt ]", end=" ")
                while True:
                    ans = input(
                        f'Are you sure you want to terminate? [Y/n] ').lower().strip()
                    if ans in ['y', 'yes']:
                        exit("[ Aborted! ]")
                    elif ans in ['n', 'no']:
                        break
                    else:
                        print(
                            "[ Invalid input ] Please try again with either 'Yes' or 'No'")
                        continue
            except KeyboardInterrupt:
                exit("[ Aborted! ]")


if __name__ == "__main__":
    user_input = get_input("Hi, how are you?")
    print("The user says,", user_input)
