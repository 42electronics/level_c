import socket                                       #make the socket module available to this program
import RPi.GPIO as GPIO                             #make the RPi.GPIO module available to this program
import time                                         #make the time module available to this program

red = 13                                            #configure GPIO13 as red LED element
green = 19                                          #configure GPIO19 as green LED element
blue = 26                                           #configure GPIO26 as blue LED element

GPIO.setmode(GPIO.BCM)                              #use BCM pin numbering scheme
GPIO.setup(red, GPIO.OUT)                           #configure red GPIO pin as output
GPIO.setup(green, GPIO.OUT)                         #configure green GPIO pin as output
GPIO.setup(blue, GPIO.OUT)                          #configure blue GPIO pin as output

SOCKPATH = "/var/run/lirc/lircd"                          #configure path for IR socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)  #configure options for IR socket
print ('Starting up on %s' % SOCKPATH)                    #print message about startup path
sock.connect(SOCKPATH)                                    #connect IR socket

def next_key():                                     #define function to get key presses
    while True:                                     #loop forever
        clear_socket = sock.recv(128)               #dump first received button to eliminate duplicates
        data = sock.recv(128)                       #receive 128 bytes from IR socket
        if data:                                    #if data is received
            break                                   #then break out of loop
    ir_data = data.split()                          #split data into list
    btn_name = ir_data[2]                           #isolate value at position 2
    btn_name = btn_name.decode("utf-8")             #convert bytes to string
    return btn_name                                 #return name of button pressed

def led_update(red_value,green_value,blue_value):   #define function to update led element states
    GPIO.output(red, red_value)                     #update red LED element
    GPIO.output(green, green_value)                 #update green LED element
    GPIO.output(blue, blue_value)                   #update blue LED element

while True:                                         #loop forever
    button = next_key()                             #call next_key function and save received info as button
    if button == 'BTN_1':                           #if name is BTN_1 then
        print('Red')                                #print Red
        led_update(1,0,0)                           #update LED for red on, green off, blue off
    elif button == 'BTN_2':                         #if name is BTN_2 then
        print('Green')                              #print Green
        led_update(0,1,0)                           #update LED for red off, green on, blue off
    elif button == 'BTN_3':                         #if name is BTN_3 then
        print('Blue')                               #print Blue
        led_update(0,0,1)                           #update LED for red off, green, off, blue on
    elif button == 'BTN_OK':                        #if name is BTN_OK then
        print('Program Exiting...')                 #print Program Exiting
        led_update(0,0,0)                           #turn off all LED elements
        GPIO.cleanup()                              #run GPIO cleanup
        raise SystemExit()                          #exit program
    else:                                           #if no other conditions were true then
        print('Button not recognized')              #print Button not recognized
        led_update(0,0,0)                           #turn off all LED elements