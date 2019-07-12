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

import time, os
from tkinter import *

root = Tk()
root.title('Photos')

def quit():
    root.destroy()
    print('Program Exiting...')
    raise SystemExit()

def update():
    global img
    timestamp = (time.strftime('%Y-%m-%d_%H:%M:%S'))
    img_file = ('/home/pi/Pictures/%s.png' % timestamp)
    os.system('raspistill -o %s -e png -w 640 -h 480' % img_file)
    print('Image saved as %s' % img_file)
    img = PhotoImage(file='%s' % img_file)
    Label(root, image=img).grid(row=0, column=0)

img = PhotoImage(file='/home/pi/Pictures/init.png')
Label(root, image=img).grid(row=0, column=0)
Button(root, text='Capture', command=update).grid(row=1, column=0)
Button(root, text='Quit', command=quit).grid(row=2, column=0)

root.mainloop()