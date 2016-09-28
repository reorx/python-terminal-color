# coding: utf-8
"""
color.py
========

Usage
-----

>>> import color
>>>
>>> # 8-bit color
>>> print red('red') + green('green') + blue('blue')
>>> print bold(yellow('bold yellow')) + underline(cyan('underline cyan'))
>>> print magenta_hl('magenta highlight')
>>>
>>> # xterm 256 color
>>> print bg256('A9D5DE', fg256('276F86', 'Info!'))
>>> print bg256('E0B4B4', fg256('912D2B', 'Warning!'))
>>> print hl256('10a3a3', 'Teal')

Note:

1. Every color function receives and returns string/unicode, so that the result
   could be used with any other strings, in any string formatting situation.

2. If you pass a str type string, the color function will return a str.
   If you pass a unicode type string, the color function will return a unicode.

3. Color functions could be composed together, like put ``red`` into ``bold``,
   or put ``bg256`` into ``fg256``. ``xxx_hl`` and ``hl256`` are mostly used
   independently.

API
---

8-bit colors:

========  ============  ===========
 Colors    Background    Highlight
========  ============  ===========
black     black_bg      black_hl
red       red_bg        red_hl
green     green_bg      green_hl
yellow    yellow_bg     yellow_hl
blue      blue_bg       blue_hl
magenta   magenta_bg    magenta_hl
cyan      cyan_bg       cyan_hl
white     white_bg      white_hl
========  ============  ===========

Styles:
- bold
- italic
- underline
- strike
- blink

.. py:function:: <color_function>(s)

   Decorate string with specified color or style.

   A color function with ``_bg`` suffix means it will set color as background.
   A color function with ``_hl`` suffix means it will set color as background,
   and change the foreground as well to make the word standout.

   :param str s: The input string (or unicode)
   :return: The decorated string (or unicode)
   :rtype: string, unicode
   :raises ValueError: if the message_body exceeds 160 characters


256 colors:
- fg256
- bg256
- hl256

.. py:function:: <256_color_function>(hexrgb, s)

   Decorate string with specified hex rgb color

   ``fg256`` will set color as foreground.
   ``bg256`` will set color as background.
   ``hg256`` will highlight input with the color.

   :param str hexrgb: The hex rgb color string, accept length 3 and 6. eg: ``555``, ``912D2B``
   :param str s: The input string (or unicode)
   :return: The decorated string (or unicode)
   :rtype: string, unicode
   :raises ValueError: If the input string's length not equal to 3 or 6.
"""

import sys


_use_color_no_tty = True


def use_color_no_tty(flag):
    global _use_color_no_tty
    _use_color_no_tty = flag


def use_color():
    if sys.stdout.isatty():
        return True
    if _use_color_no_tty:
        return True
    return False


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


###############################################################################
# 8 bit Color
###############################################################################

def make_color(start, end):
    def color_func(s):
        if not use_color():
            return s

        s, utf8 = to_unicode(s)

        # render
        f = start + s + end

        if utf8:
            f = f.encode('utf8')
        return f

    return color_func


# According to https://en.wikipedia.org/wiki/ANSI_escape_code#graphics ,
# 39 is reset for foreground, 49 is reset for background, 0 is reset for all
# we can use 0 for convenience, but it will make color combination behaves weird.
END = esc(0)

FG_END = esc(39)
black = make_color(esc(30), FG_END)
red = make_color(esc(31), FG_END)
green = make_color(esc(32), FG_END)
yellow = make_color(esc(33), FG_END)
blue = make_color(esc(34), FG_END)
magenta = make_color(esc(35), FG_END)
cyan = make_color(esc(36), FG_END)
white = make_color(esc(37), FG_END)

BG_END = esc(49)
black_bg = make_color(esc(40), BG_END)
red_bg = make_color(esc(41), BG_END)
green_bg = make_color(esc(42), BG_END)
yellow_bg = make_color(esc(43), BG_END)
blue_bg = make_color(esc(44), BG_END)
magenta_bg = make_color(esc(45), BG_END)
cyan_bg = make_color(esc(46), BG_END)
white_bg = make_color(esc(47), BG_END)

HL_END = esc(22, 27, 39)
#HL_END = esc(22, 27, 0)

black_hl = make_color(esc(1, 30, 7), HL_END)
red_hl = make_color(esc(1, 31, 7), HL_END)
green_hl = make_color(esc(1, 32, 7), HL_END)
yellow_hl = make_color(esc(1, 33, 7), HL_END)
blue_hl = make_color(esc(1, 34, 7), HL_END)
magenta_hl = make_color(esc(1, 35, 7), HL_END)
cyan_hl = make_color(esc(1, 36, 7), HL_END)
white_hl = make_color(esc(1, 37, 7), HL_END)

bold = make_color(esc(1), esc(22))
italic = make_color(esc(3), esc(23))
underline = make_color(esc(4), esc(24))
strike = make_color(esc(9), esc(29))
blink = make_color(esc(5), esc(25))


###############################################################################
# Xterm 256 Color (delete if you don't need)
###############################################################################
#
# Rewrite from: https://gist.github.com/MicahElliott/719710

import re  # NOQA

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


class Memorize(dict):
    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


def memorize(func):
    func._cache = {}

    def wrapper(*args, **kwargs):
        if kwargs:
            return func(*args, **kwargs)
        if args not in func._cache:
            func._cache[args] = func(*args, **kwargs)
        return func._cache[args]

    for i in ('__module__', '__name__', '__doc__'):
        setattr(wrapper, i, getattr(func, i))
    wrapper.__dict__.update(getattr(func, '__dict__', {}))
    wrapper._origin = func
    return wrapper


@memorize
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


@memorize
def hex_to_rgb(hx):
    hxlen = len(hx)
    if hxlen != 3 and hxlen != 6:
        raise ValueError('hx color must be of length 3 or 6')
    if hxlen == 3:
        hx = ''.join(i * 2 for i in hx)
    parts = [int(h, 16) for h in re.split(r'(..)(..)(..)', hx)[1:4]]
    return tuple(parts)


def make_256(start, end):
    def rgb_func(rgb, s, x=None):
        if not use_color():
            return s

        s, utf8 = to_unicode(s)

        # render
        if isinstance(rgb, tuple):
            pass
        elif isinstance(rgb, str):
            rgb = hex_to_rgb(rgb)
        else:
            raise ValueError('rgb should be either tuple or str')
        if x is not None:
            xcolor = x
        else:
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
hl256 = make_256(esc(1, 38, 5, '{x}', 7), esc(27, 39, 22))

_grayscale_xterm_codes = [int(i) for i, _ in _GRAYSCALE]
grayscale = {(i - _grayscale_xterm_codes[0]): make_color(esc(38, 5, i), esc(39)) for i in _grayscale_xterm_codes}
grayscale_bg = {(i - _grayscale_xterm_codes[0]): make_color(esc(48, 5, i), esc(49)) for i in _grayscale_xterm_codes}
grayscale_hl = {(i - _grayscale_xterm_codes[0]): make_color(esc(1, 38, 5, i, 7), esc(27, 39, 22)) for i in _grayscale_xterm_codes}
