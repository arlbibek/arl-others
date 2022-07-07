from sys import argv
import requests


def getRandNumOf(n):
    '''Returns randomly generated number with length of n'''
    import random
    return str(random.randrange(int(f'1{"0" * (n-1)}'), int(f'1{"0" * n}')))


def getRandomImageLink(n=1, width=1920, height=1080):
    '''generated random image link'''
    return f'https://picsum.photos/{width}/{height}?random={n}'


def get_img_ext(url):
    '''Extracts and returns extension from url such as https://i.picsum.photos/id/110/1920/1080.jpg?hmac=iK7v9di6IQ0YMzcnkQ1aX7oXYb88N3QM017gbIJ4poM'''
    from os.path import splitext

    return splitext(url.split("?")[0])[-1]


def image_dl(link, img_dir):
    "Download image from url"
    from os import mkdir
    from os.path import join, exists

    url = requests.get(link).url
    ext = get_img_ext(url)

    # directory to store all downloaded images
    if not exists(img_dir):
        mkdir(img_dir)
    while True:
        img_name = f'{getRandNumOf(6)}{ext}'
        img_path = join(img_dir, img_name)
        if not exists(img_path):
            break
    with open(img_path, "wb") as ib:
        ib.write(requests.get(url).content)
    print(img_name)


if __name__ == "__main__":
    print("\n\t'''Download random HD images from picsum.photos'''\n")

    n = argv[1].strip().strip(
        "-").strip("--") if len(argv) > 1 else None

    img_dir = "random_images"

    while True:
        if n is None:
            try:
                n = input("how many images?: ")
            except KeyboardInterrupt:
                exit('Abort!')
        try:
            n = int(n)
        except ValueError:
            pass
        if isinstance(n, int):
            break
        n = None
        print("\nPlease enter an integer value (CTRL + C is exit)")
    downloads = 0
    if not n < 1:
        for i in range(1, n+1):
            try:
                print(f'{i}/{n}', end="\r")
                link = getRandomImageLink(i)
                image_dl(link, img_dir)
                downloads += 1
            except KeyboardInterrupt as e:
                print("Abort!")
                break
            except Exception as e:
                print(e)
                break
        print(
            f"\n[ done ] {downloads} random {'images' if downloads > 1 else 'image'} downloaded, check '{img_dir}'\n")
        print("Do not forget to check out: https://picsum.photos\n")
    else:
        print(f"[ done ] nothing to download")
