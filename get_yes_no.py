'''this is a simpel function to get 'True' or 'False' ans from the user'''


def ynq(question):
    while True:
        print()
        ans = input(str(question) + '(y/n): ')
        if ans == 'y' or ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'YES':
            return True
        elif ans == 'n' or ans == 'N' or ans == 'no' or ans == 'No' or ans == 'NO':
            return False
        elif ans == '':
            print("Don't leave the field empty!")
        else:
            print("Invalid Input!!\nEnter 'y' for 'Yes' or 'n' for 'No'")
            continue


print(ynq("Is the sky blue?: "))
