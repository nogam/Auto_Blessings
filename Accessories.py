import os.path
from numpy import random as npr


def is_file_exists (path):
    return os.path.exists(path)

def generate_font_color():
    color1 = ''
    color2 = ''
    result = []

    color = npr.choice(range(256), size=3)
    for rgb in color:
        color1 = color1 + str(rgb) + ','
        color2 = color2 + str(abs(255 - rgb)) + ','

    result.append('(' + color1[:-1] + ')')
    result.append('(' + color2[:-1] + ')')
    return result

def get_font_size(height, width):
    return None

def get_font():
    return None

