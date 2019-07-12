#Copyright (c) 2019 42 Development dba 42 Electronics
#Author: Eric Feickert
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import requests

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)

disp.begin()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',18)

def update_color():
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    feed = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json')
    data = feed.json()
    current = data['field1']
    return(current)
try:
    while True:
        color = update_color()
        draw.text((0, 0), 'Cheerlights', font=font, fill=255)
        draw.text((0, 22), 'color is:', font=font, fill=255)
        draw.text((0, 44), color, font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(30)
except KeyboardInterrupt:
    disp.clear()
    disp.display()
    SystemExit()