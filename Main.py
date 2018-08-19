# -*- coding: utf-8 -*-

from image import getImage as img
from text import getText as txt
from GlobalVars import TIME_STAMP
import Accessories as acs

def generate_greeting():
    return None


if __name__ == '__main__':
    ts = TIME_STAMP

    path = img.getimage(ts)

    print path
    print txt.get_text()
    print acs.is_file_exists(path)


    print acs.generate_font_color()