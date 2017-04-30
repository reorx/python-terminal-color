# coding: utf-8

# Default color levels for the color cube
cubelevels = [0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff]
# Generate a list of midpoints of the above list
snaps = [(x + y) / 2 for x, y in zip(cubelevels, [0] + cubelevels)[1:]]

_gray_scale = [
    # Gray-scale range.
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

gray_scale = {int(b[:2], 16): a for a, b in _gray_scale}
gray_scale_points = gray_scale.keys()


def get_closest(v, l):
    return min(l, key=lambda x: abs(x - v))


def rgb2short(r, g, b):
    """ Converts RGB values to the nearest equivalent xterm-256 color.
    """
    if r == g == b:
        # use gray scale
        gs = get_closest(r, gray_scale_points)
        return gray_scale[gs]
    # Using list of snap points, convert RGB value to cube indexes
    r, g, b = map(lambda x: len(tuple(s for s in snaps if s < x)), (r, g, b))
    # Simple colorcube transform
    return r * 36 + g * 6 + b + 16


def hex2parts(hex):
    parts = [int(h, 16) for h in re.split(r'(..)(..)(..)', hex)[1:4]]
    return parts


if __name__ == '__main__':
    import re
    import sys
    from colortrans import CLUT

    #for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
    #    hex = i * 6
    #    parts = hex2parts(hex)
    #    #print parts

    #    term = rgb2short(parts[0], parts[1], parts[2])
    #    sys.stdout.write('RGB %s -> xterm color approx \033[38;5;%sm%s (%s)' % (parts, term, term, hex))
    #    sys.stdout.write("\033[0m\n")

    for v, hex in CLUT:
        parts = hex2parts(hex)
        term = rgb2short(parts[0], parts[1], parts[2])
        sys.stdout.write('RGB %s -> xterm color (%s) \033[38;5;%sm%s (%s)' % (parts, v, term, term, hex))
        sys.stdout.write("\033[0m\n")
