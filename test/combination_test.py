# coding: utf-8

import color


def test_combination():
    print()
    tpl = color.green('the quick {} jump over the {} dog')
    f = tpl.format(
        color.yellow('brown fox'),
        color.red_bg('lazy'),
    )
    print(repr(f))
    print(f)

    tpl = color.green_bg('the quick {} jump over the {} dog')
    f = tpl.format(
        color.yellow('brown fox'),
        color.red_bg('lazy'),
    )
    print(repr(f))
    print(f)
