import RPi.GPIO as GPIO
import time
from mpu6050 import mpu6050

servo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

sensor = mpu6050(0x68)

servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)

try:
    while True:
        data = sensor.get_accel_data()
        y_accel = data['y']
        if 14 > y_accel >= 0:
            dc = 7 - (y_accel * 0.5)
        elif -14 < y_accel < 0:
            dc = 7 + (y_accel * -0.5)
        else:
            pass
        servo_pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
		
except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()