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

import socket
import RPi.GPIO as GPIO
import time
import os

red = 13
green = 19
blue = 26
servo = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

SOCKPATH = "/var/run/lirc/lircd"
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print ('Starting up on %s' % SOCKPATH)
sock.connect(SOCKPATH)

def next_key():
    while True:
        clear_socket = sock.recv(128)
        data = sock.recv(128)
        if data:
            break
    ir_data = data.split()
    btn_name = ir_data[2]
    btn_name = btn_name.decode("utf-8")
    return btn_name

def led_update(red_value,green_value,blue_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)

servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)

while True:
    button = next_key()    
    if button == 'BTN_1':
        print('Red')
        led_update(1,0,0)
    elif button == 'BTN_2':
        print('Green')
        led_update(0,1,0)
    elif button == 'BTN_3':
        print('Blue')
        led_update(0,0,1)
    elif button == 'BTN_4':
        led_update(0,0,0)
        os.system("gpio -g mode 18 ALT5")
        os.system("aplay /home/pi/hello_42.wav")
        os.system("gpio -g mode 18 in")
    elif button == 'BTN_LEFT':
        print('Servo Left')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(12.5)
    elif button == 'BTN_UP':
        print('Servo Middle')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(7)
    elif button == 'BTN_RIGHT':
        print('Servo Right')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(2.5)
    elif button == 'BTN_OK':
        print('Program Exiting...')
        led_update(0,0,0)
        servo_pwm.stop()
        GPIO.cleanup()
        raise SystemExit()
    else:
        print('Button not recognized')
        led_update(0,0,0)
