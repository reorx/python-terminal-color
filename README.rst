Python Terminal Color
=====================

Introduction
------------

1. This is a drop-in library for print colorized output in termianl.
2. It has no pypi package, which means you can't install it through pip.
3. It is recommended to be copied to your own project as a submodule so that
   no dependency will be involved.
4. The reason why 


Usage
-----

Copy the ``color.py`` file to your project, then:

.. code:: python

    from yourproject import color

    # 8 bit color
    print color.red('red') + color.green('green') + color.blue('blue')
    print color.bold(color.yellow('bold yellow')) + color.underline(color.cyan('underline cyan'))
    print color.magenta_hl('magenta highlight')

    # xterm 256 color
    print color.bg256('A9D5DE', color.fg256('276F86', 'Info!'))
    print color.bg256('E0B4B4', color.fg256('912D2B', 'Warning!'))
    print color.hl256('10a3a3', 'Teal')


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


``<color_function>(s)``
~~~~~~~~~~~~~~~~~~~~~~~

Decorate string with specified color.

``color_function`` is one of below function names:

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

A color function with ``_bg`` suffix means it will set color as background.
A color function with ``_hl`` suffix means it will set color as background,
and change the foreground as well to make the word standout.

Parameters:

- :param str s: The input string (or unicode)
- :return: The decorated string (or unicode)
- :rtype: string, unicode
- :raises ValueError: if the message_body exceeds 160 characters

``<style_function>(s)``
~~~~~~~~~~~~~~~~~~~~~~~

Decorate string with specified style.

``style_function`` is one of below function names:

- bold
- italic
- underline
- strike
- blink

Arguments and return are the same as ``color_function``.


``<256_color_function>(hexrgb, s)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decorate string with specified hex rgb color

``256_color_function`` is one of below function names:

- fg256: will set color as foreground.
- bg256: will set color as background.
- hl256: will highlight input with the color.

Parameters:

- :param str hexrgb: The hex rgb color string, accept length 3 and 6. eg: ``555``, ``912D2B``
- :param str s: The input string (or unicode)
- :return: The decorated string (or unicode)
- :rtype: string, unicode
- :raises ValueError: If the input string's length not equal to 3 or 6.
