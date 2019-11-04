# coding: utf-8

import color

color_names = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


def test_named_colors():
    for i in color_names:
        print(getattr(color, i)(i) + color.red('compare'))
        print(color.black(getattr(color, i + '_bg')(i + '_bg')) + color.red('compare'))
        print(getattr(color, i + '_hl')(i + '_hl') + color.red('compare'))


def test_decorations():
    for i in ['bold', 'italic', 'underline', 'strike', 'blink']:
        print('#' + i)
        for j in color_names:
            c = getattr(color, j)(j)
            print(getattr(color, i)(c) + color.red('compare'))


def test_256_colors():
    for i in (range(10) + ['a', 'b', 'c', 'd', 'e', 'f']):
        hex = str(i) * 3
        print(color.fg256(hex, hex), color.bg256(hex, hex), color.hl256(hex, hex))


def test_grayscale():
    for i in sorted(color.grayscale):
        print(color.grayscale[i]('grayscale' + str(i)))
    for i in sorted(color.grayscale):
        print(color.grayscale_bg[i]('grayscale_bg' + str(i)))
    for i in sorted(color.grayscale):
        print(color.grayscale_hl[i]('grayscale_hl' + str(i)))
