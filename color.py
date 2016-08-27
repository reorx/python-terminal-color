# coding: utf-8

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

import re


def esc(*codes):
    """Produces an ANSI escape code unicode from a list of integers"""
    return u'\x1b[%sm' % (u';'.join([unicode(c) for c in codes]))


def to_unicode(s):
    utf8 = False
    if isinstance(s, str):
        utf8 = True
        s = s.decode('utf8')
    if not isinstance(s, unicode):
        raise TypeError('either str or unicode is allowed')
    return s, utf8


def make_color(start, end):
    def color_func(s):
        s, utf8 = to_unicode(s)

        # render
        f = start + s + end

        if utf8:
            f = f.encode('utf8')
        return f

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
strike = make_color(esc(9), esc(29))
blink = make_color(esc(5), esc(25))


###############################################################################
# Xterm 256 Color (delete if you don't need)
###############################################################################
#
# Code from: https://gist.github.com/MicahElliott/719710

# Default color levels for the color cube
CUBELEVELS = [0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff]

# Generate a list of midpoints of the above list
SNAPS = [(x + y) / 2 for x, y in zip(CUBELEVELS, [0] + CUBELEVELS)[1:]]

# Gray-scale range.
_GRAYSCALE = [
    ('232', '080808'),
    ('233', '121212'),
    ('234', '1c1c1c'),
    ('235', '262626'),
    ('236', '303030'),
    ('237', '3a3a3a'),
    ('238', '444444'),
    ('239', '4e4e4e'),
    ('240', '585858'),
    ('241', '626262'),
    ('242', '6c6c6c'),
    ('243', '767676'),
    ('244', '808080'),
    ('245', '8a8a8a'),
    ('246', '949494'),
    ('247', '9e9e9e'),
    ('248', 'a8a8a8'),
    ('249', 'b2b2b2'),
    ('250', 'bcbcbc'),
    ('251', 'c6c6c6'),
    ('252', 'd0d0d0'),
    ('253', 'dadada'),
    ('254', 'e4e4e4'),
    ('255', 'eeeeee'),
]

GRAYSCALE = {int(b[:2], 16): a for a, b in _GRAYSCALE}
GRAYSCALE_POINTS = GRAYSCALE.keys()


def get_closest(v, l):
    return min(l, key=lambda x: abs(x - v))


def rgb_to_xterm(r, g, b):
    """ Converts RGB values to the nearest equivalent xterm-256 color.
    """
    if r == g == b:
        # use gray scale
        gs = get_closest(r, GRAYSCALE_POINTS)
        return GRAYSCALE[gs]
    # Using list of snap points, convert RGB value to cube indexes
    r, g, b = map(lambda x: len(tuple(s for s in SNAPS if s < x)), (r, g, b))
    # Simple colorcube transform
    return r * 36 + g * 6 + b + 16


def hex_to_rgb(hx):
    hxlen = len(hx)
    if hxlen != 3 and hxlen != 6:
        raise ValueError('hx color must be of length 3 or 6')
    if hxlen == 3:
        hx = ''.join(i * 2 for i in hx)
    parts = [int(h, 16) for h in re.split(r'(..)(..)(..)', hx)[1:4]]
    return tuple(parts)


def make_256(start, end):
    def rgb_func(hx, s):
        s, utf8 = to_unicode(s)

        # render
        rgb = hex_to_rgb(hx)
        xcolor = rgb_to_xterm(*rgb)

        tpl = start + u'{s}' + end
        f = tpl.format(
            x=xcolor,
            s=s)

        if utf8:
            f = f.encode('utf8')
        return f

    return rgb_func


fg256 = make_256(esc(38, 5, '{x}'), esc(39))
bg256 = make_256(esc(48, 5, '{x}'), esc(49))
