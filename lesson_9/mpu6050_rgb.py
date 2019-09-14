import RPi.GPIO as GPIO
import time
from mpu6050 import mpu6050

red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)
	
sensor = mpu6050(0x68)

try:
    while True:
        data = sensor.get_accel_data()
        y_accel = data['y']
        if y_accel > 4:
            led_update(1,0,0)
        elif y_accel < -4:
            led_update(0,0,1)
        else:
            led_update(0,1,0)
        time.sleep(0.05)
		
except KeyboardInterrupt:
    led_update(0,0,0)
    GPIO.cleanup()