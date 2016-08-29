# coding: utf-8

import color


def test_notty():
    """
    Run `nosetests -vs test/notty_test.py | less` to see red is not red
    """
    color.use_color_no_tty(False)
    print color.red('red')
