# coding: utf-8

import color
import time


rgb_tuple = (100, 150, 200)


def with_memorize_test():
    print 'Run 10000 times'
    t0 = time.time()
    for _ in xrange(10000):
        color.rgb_to_xterm(*rgb_tuple)
    tr = int((time.time() - t0) * 1000)
    print 'Cost {} ms'.format(tr)


def without_memorize_test():
    print 'Run 10000 times'
    t0 = time.time()
    for _ in xrange(10000):
        color.rgb_to_xterm._origin(*rgb_tuple)
    tr = int((time.time() - t0) * 1000)
    print 'Cost {} ms'.format(tr)
