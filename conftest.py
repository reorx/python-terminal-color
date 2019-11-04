import os
import sys


if os.getenv('COLOR_COMPAT'):
    print('use color_compat.py')
    import color_compat
    sys.modules['color'] = sys.modules['color_compat']
else:
    print('use color.py')
