import os
import sys

def color(text, color_code):
    """Colorize text.
    @param text: text.
    @param color_code: color.
    @return: colorized text.
    """
    # $TERM under Windows:
    # cmd.exe -> "" (what would you expect..?)
    # cygwin -> "cygwin" (should support colors, but doesn't work somehow)
    # mintty -> "xterm" (supports colors)
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text
    return "\x1b[%dm%s\x1b[0m" % (color_code, text)

