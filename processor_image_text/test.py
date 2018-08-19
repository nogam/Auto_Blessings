# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import Accessories as acs
from text import getText as txt


my_text = txt.get_heb_text()

image = Image.open('C:/Code Projects/SillyGreetings/output/input_1533402088.jpg')

#set fonts properties
colors = acs.generate_font_color()

font_size = 100
my_font = 'fonts/VarelaRound-Regular.ttf'
font_type = ImageFont.truetype(font=my_font, size=font_size, encoding='utf-8')

draw = ImageDraw.Draw(image)

x, y = 10, 10 #text location point

#add font shadow color
margin = font_size*0.015
draw.text((x-margin, y-margin), text=my_text, font=font_type, fill='rgb'+colors[0])
draw.text((x+margin, y-margin), text=my_text, font=font_type, fill='rgb'+colors[0])
draw.text((x+margin, y-margin), text=my_text, font=font_type, fill='rgb'+colors[0])
draw.text((x-margin, y+margin), text=my_text, font=font_type, fill='rgb'+colors[0])

#add font main color
draw.text(xy=(x,y), text=my_text, font=font_type, fill='rgb'+colors[1])

image.show()