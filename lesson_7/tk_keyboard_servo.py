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

from tkinter import Tk
import RPi.GPIO as GPIO

servo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)

def on_close():
    print('Quitting Program...')
    servo_pwm.stop()
    GPIO.cleanup()
    root.destroy()

def key_input(event):
    if event.char == 'a':
        print('a pressed')
        servo_pwm.ChangeDutyCycle(12.5)
    elif event.char == 's':
        print('s pressed')
        servo_pwm.ChangeDutyCycle(9.2)
    elif event.char == 'd':
        print('d pressed')
        servo_pwm.ChangeDutyCycle(5.8)
    elif event.char == 'f':
        print('f pressed')
        servo_pwm.ChangeDutyCycle(2.5)
    elif event.char == 'q':
        on_close()
    else:
        print('Invalid input')

root = Tk()
root.bind('<KeyPress>', key_input)
root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
