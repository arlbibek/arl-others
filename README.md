# ⚙️ Automating the Boring Stuff with Python

↓ Read to know what each file does. ↓

## add_num.py

Add an auto increment numbers on each lines of a text file.

```text
Eg.
    From:
        This is line one
        This a second line
        3. I'm line three
        Yay Fourth
    To:
        1. This is line one
        2. This a second line
        3. I'm line three
        4. Yay Fourth
```

## auto_wr_txt.py

Auto write text with `pyautogui`

Options

1. Write contains of the clipboard.
2. Write contents of a text file.
3. Write contents of the text provided by the user.

```text
# Requirements
pyautogui & pyperclip

# local dependencies
get_input() from get_input.py
get_filepath() from get_path.py
```

## bored.py

Run this if you get bored!

## create_file.py

Instantly create a file of any size (in GB).

## generate_2fa_codes.py

Instantly create a text file with 6 digit two factor authentication codes.

## get_files.py

Returns the list of every file in a directory tree.

## get_path.py

Get either file or directory path from the user.

```python
get_filepath()
# Returns the absolute path of a file.

get_dirpath()
# Returns the absolute path of a directory.
```

## get_yes_no.py

Returns `True` if input from the user is `yes`, `False` if `no`, that is all.

## refreshWin.py

> Requirement: `pyautogui`

A simple and fun program that refresh windows any numbers of times you want.

## rename_files.py

Rename all file on a folder to randomly generated 6 digit code.

```text
From:
    __fjdsl7439fRHzzt77UUvfTRe7362.png
To:
    544305.png
```

## sort_txt.py

Sort contents of a text file into ascending or descending order.

## timer.py

A cli timer that prints like clock ticking.

## remove_lines.py

Remove certain line from a text file.

```python
rm_duplicate_lines(filepath)
# Remove duplicate lines from a (text) file.

rm_less_than(n, filepath)
# Remove lines with less than n (n = length of a character) numbers of characters from a file.
```

## sync_files.py

Move all files from a directory tree to single directory.

```text
From:
    src
    |---dir1
    |   |---file1
    |   |---file2
    |---dir2
    |   |---dir3
    |   |   |---dir3
    |   |   |   |---file3
    |   |   |   |---file4
    |---dir4
    |   |---file4
    |   |---file5
    |---file3
    |---file5

To:
    dist
    |---file1
    |---file2
    |---file3
    |---file4
    |---file5
```

## images_dl.py

> Requirement: `requests`

Download random HD images from [picsum.photos](https://picsum.photos)

## get_input.py

Returns a valid input from the user.

## type_wr

Prints string in a type writer effect.

---

Made with ❤️ by [Bibek Aryal](https://bibeka.com.np/).
