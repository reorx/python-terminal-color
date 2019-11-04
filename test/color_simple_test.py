# coding: utf-8

import color_simple

color_names = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

compare = color_simple.red('compare') + 'white'


def test_colors():
    for i in color_names:
        print(getattr(color_simple, i)(i) + compare)


def test_styles():
    for i in ('bold', 'underline'):
        print(getattr(color_simple, i)(i) + compare)


def test_grayscale():
    print()
    for i in sorted(color_simple.grayscale.keys()):
        print(color_simple.grayscale[i]('grayscale {}'.format(i)) + compare)
