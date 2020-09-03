from PIL import Image, ImageDraw
from math import*
I, k, l, m, n, o, _ = Image.new('P', (394, 480)), 479, 180, 465, 232, 347, 255
D = ImageDraw.Draw(I)
P, G = D.polygon, D.pieslice
I.putpalette([_, _, _, 0, 0, _, _, 20, 60])


def S(x, y, r, e, l, b):
    p, a, h = [], 2 * pi / e, r * l
    c, d = [0, -a / 2][b], [a / 2, 0][b]
    for i in range(e):
        p += [(x + r * cos(i * a + c), y + r * sin(i * a + c)),
              (x + h * cos(i * a + d), y + h * sin(i * a + d))]
    P(p, fill=0)


P([(0, 0), (393, 246), (144, 246), (375, k), (0, k)], fill=1)
P([(14, 25), (o, n), (110, n), (o, m), (14, m)], fill=2)
S(96, o, 68, 12, .6, 0)
G([(31, 90), (163, 221)], 0, l, fill=0)
G([(28, 68), (166, 200)], 0, l, fill=2)
S(96, 178, 40, 16, .7, 1)
I.show()
