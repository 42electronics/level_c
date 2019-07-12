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

from bottle import route, run
import RPi.GPIO as GPIO

red = 13
green = 19
blue = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def led_update(red_value,green_value,blue_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
    <h1>RGB LED</h1>
    <p>Click the links below to change the LED color</p>
    <a href="/red_on">Red</a>
    <br>
    <a href="/green_on">Green</a>
    <br>
    <a href="/blue_on">Blue</a>
    <br>
    <br>
    <a href="/cleanup">GPIO Cleanup</a>
    </body>
</html>
'''

@route('/red_on')
def red_on():
    led_update(1,0,0)
    return "Red On"

@route('/green_on')
def green_on():
    led_update(0,1,0)
    return "Green On"

@route('/blue_on')
def blue_on():
    led_update(0,0,1)
    return "Blue On"

@route('/cleanup')
def cleanup():
    led_update(0,0,0)
    GPIO.cleanup()
    return "GPIO Cleanup Completed"

run(host='your_ip_address', port=8080)
