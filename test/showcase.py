# coding: utf-8

from __future__ import print_function
import color
from rgbxterm_test import CLUT


color_names = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


def static_width(s, width, length=None):
    if length is None:
        length = len(s)
    return s + (' ' * (width - length))


if __name__ == '__main__':
    print()
    print('{} {} {}'.format(
        static_width('color(s)', 8),
        static_width('color_bg(s)', 12),
        static_width('color_hl(s)', 12),
    ))
    for i in color_names:
        t0 = i
        t1 = i + '_bg'
        t2 = i + '_hl'
        print('{} {} {}'.format(
            static_width(getattr(color, t0)(t0), 8, len(t0)),
            static_width(getattr(color, t1)(t1), 12, len(t1)),
            static_width(getattr(color, t2)(t2), 12, len(t2)),
        ))
    print()

    s = ''.join(color.grayscale_bg[i](' ') for i in color.grayscale_bg)
    print('grayscale_bg() {}'.format(s))
    print()

    print('                 bg256(hex, s)')
    clut = CLUT[16:-24]
    rl = 6
    while clut:
        r = clut[:rl]
        clut = clut[rl:]

        s = ''.join(color.bg256(hex, '  ') for _, hex in r)
        print('{} ~ {}: {}'.format(r[0][1], r[-1][1], s))
        # s = ''.join(color.bg256(hex, '  ', x=x) for x, hex in r)
