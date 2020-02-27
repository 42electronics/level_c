import RPi.GPIO as GPIO
import Adafruit_SSD1306
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import time, os, ultrasonic, _thread

red = 13
green = 19
sensitivity = 50
armed = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
disp.begin()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',24)

root = Tk()
root.title('Alarm System')

def audio_alert():
    os.system("gpio -g mode 18 ALT5")
    os.system("aplay /home/pi/alarm/alarm.wav")
    os.system("gpio -g mode 18 in")

def led_update(red_value,green_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    
def display_update(line1,line2):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 0), line1, font=font, fill=255)
    draw.text((0, 22), line2, font=font, fill=255)
    disp.image(image)
    disp.display()
    
def update():
    global img
    timestamp = (time.strftime('%Y-%m-%d_%H:%M:%S'))
    img_file = ('/home/pi/Pictures/captures/%s.png' % timestamp)
    os.system('raspistill -o %s -e png -w 640 -h 480 -t 1500' % img_file)
    print('Image saved as %s' % img_file)
    img = PhotoImage(file='%s' % img_file)
    Label(root, image=img).grid(row=0, column=0)
    
def proximity():
    while armed == 1:
        distance = ultrasonic.average()
        if distance < sensitivity:
            timestamp = time.strftime('%H:%M:%S')
            display_update('ALARM at ', timestamp)
            _thread.start_new_thread(audio_alert, ())
            update()
        time.sleep(0.1)
        
def arm():
    global armed
    global img
    armed = 1
    led_update(1,0)
    img = PhotoImage(file='/home/pi/alarm/armed.png')
    Label(root, image=img).grid(row=0, column=0)
    display_update('ARMED','')
    _thread.start_new_thread(proximity, ())
    
def disarm():
    global armed
    global img
    armed = 0
    led_update(0,1)
    img = PhotoImage(file='/home/pi/alarm/disarmed.png')
    Label(root, image=img).grid(row=0, column=0)
    display_update('DISARMED','')
    
def quit():
    raise SystemExit()
    
try:
    disarm()
    Label(root, image=img).grid(row=0, column=0)
    Button(root, text="Arm", command=arm, width=5).grid(row=1, column=0)
    Button(root, text="Disarm", command=disarm, width=5).grid(row=2, column=0)
    Button(root, text="Quit", command=quit, width=5).grid(row=3, column=0)
    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()
    
except (KeyboardInterrupt, SystemExit):
    led_update(0,0)
    root.destroy()
    disp.clear()
    disp.display()
    GPIO.cleanup()