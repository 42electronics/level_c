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

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
        <h1>RGB LED</h1>
        <p>Click the links below to change the LED color</p>
        <a href="/red_on">Red On</a>
        <br>
        <br>
        <a href="/red_off">Red Off</a>
    </body>
</html>
'''

@route('/red_on')
def red_on():
    GPIO.output(13, GPIO.HIGH)
    return "Red On"

@route('/red_off')
def red_off():
    GPIO.output(13, GPIO.LOW)
    return "Red"

run(host='your_ip_address', port=8080)