# coding: utf-8

import color_simple

color_names = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


def test_color_simple():
    for i in color_names:
        print getattr(color_simple, i)(i) + color_simple.red('compare') + 'white'
    for i in ('bold', 'underline'):
        print getattr(color_simple, i)(i) + color_simple.red('compare') + 'white'
