# coding: utf-8

import sys
import functools

from fabulous import utils, xterm256, grapefruit

#red
#green
#blue
#yellow
#magenta
#cyan
#black
#white
#gray

#_bg

#fg256
#bg256

#bold
#italic
#underline


try:
    unicode = unicode
except NameError:
    unicode = str
    basestring = (str, bytes)


OVERLINE = u'\u203e'


def esc(*codes):
    """Produces an ANSI escape code unicode from a list of integers"""
    return u'\x1b[%sm' % (u';'.join([unicode(c) for c in codes]))


def make_color(start, end):
    def color_func(s):
        utf8 = False
        if isinstance(s, str):
            utf8 = True
            s = s.decode('utf8')
        if not isinstance(s, unicode):
            raise TypeError('input either str or unicode for color function')

        c = start + s + end
        if utf8:
            c = c.encode('utf8')
        return c

    return color_func


# According to https://en.wikipedia.org/wiki/ANSI_escape_code#graphics ,
# end seems could be both 0 and 39
#END = esc(39)
END = esc(0)

black = make_color(esc(30), END)
red = make_color(esc(31), END)
green = make_color(esc(32), END)
yellow = make_color(esc(33), END)
blue = make_color(esc(34), END)
magenta = make_color(esc(35), END)
cyan = make_color(esc(36), END)
white = make_color(esc(37), END)

# From http://askubuntu.com/a/528938/136672 , end = 0 is OK
bold = make_color(esc(1), esc(22))
italic = make_color(esc(3), esc(23))
underline = make_color(esc(4), esc(24))
