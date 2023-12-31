# servo motion

# import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import paho.mqtt.client as mqtt
import uuid
import time

from adafruit_servokit import ServoKit
#
# topic = 'IDD/body_position'
# body_position = 'Not read'

# # Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# # Name and set up the servo according to the channel you are using.
servo_upper_0 = kit.servo[0]
servo_bottom_0 = kit.servo[1]
servo_upper_1 = kit.servo[2]
servo_bottom_1 = kit.servo[3]
servo_upper_2 = kit.servo[12]
servo_bottom_2 = kit.servo[13]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
# servo_shadow.set_pulse_width_range(500, 2500)


# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
#
body_position = ['left','middle','right']

def push_shadow_tile(condition):

    show_add = -3
    no_show_add = 3
    outside = 5
    inside = 175
    sleep_time = 0.02

    if condition == 'left':

        # push postion 0 out, pull others in.
        while servo_upper_0.angle > outside:
            servo_upper_0.angle += show_add
            servo_bottom_0.angle += show_add

            if servo_upper_1.angle < inside:
                servo_upper_1.angle += no_show_add
                servo_bottom_1.angle += no_show_add

            if servo_upper_2.angle < inside:
                servo_upper_2.angle += no_show_add
                servo_bottom_2.angle += no_show_add

            time.sleep(sleep_time)

    elif condition == 'middle':
        while servo_upper_1.angle > outside:
            servo_upper_1.angle += show_add
            servo_bottom_1.angle += show_add

            if servo_upper_0.angle < inside:
                servo_upper_0.angle += no_show_add
                servo_bottom_0.angle += no_show_add

            if servo_upper_2.angle < inside:
                servo_upper_2.angle += no_show_add
                servo_bottom_2.angle += no_show_add
            time.sleep(sleep_time)

    elif condition == 'right':
        while servo_upper_2.angle > outside:
            servo_upper_2.angle += show_add
            servo_bottom_2.angle += show_add

            if servo_upper_1.angle < inside:
                servo_upper_1.angle += no_show_add
                servo_bottom_1.angle += no_show_add

            if servo_upper_0.angle < inside:
                servo_upper_0.angle += no_show_add
                servo_bottom_0.angle += no_show_add

            time.sleep(sleep_time)

    else:
        while servo_upper_0.angle < inside or servo_upper_1.angle < inside or servo_upper_2.angle < inside:
            servo_upper_2.angle += no_show_add
            servo_bottom_2.angle += no_show_add

            if servo_upper_1.angle < inisde:
                servo_upper_1.angle += no_show_add
                servo_bottom_1.angle += no_show_add

            if servo_upper_0.angle < inisde:
                servo_upper_0.angle += no_show_add
                servo_bottom_0.angle += no_show_add

            time.sleep(sleep_time)


servo_upper_0.angle = 165
servo_bottom_0.angle = 165
servo_upper_1.angle = 165
servo_bottom_1.angle = 165
servo_upper_2.angle = 165
servo_bottom_2.angle = 165

while True:

    try:

        print("pushing left")
        push_shadow_tile('left')
        print("pushing middle")
        push_shadow_tile('middle')
        print("pushing right")
        push_shadow_tile('right')

        print("pushing left")
        push_shadow_tile('left')
        print("pushing middle")
        push_shadow_tile('middle')
        print("pushing right")
        push_shadow_tile('right')


    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position

        servo_upper_0.angle = 180
        servo_bottom_0.angle = 180
        servo_upper_1.angle = 180
        servo_bottom_1.angle = 180
        servo_upper_2.angle = 180
        servo_bottom_2.angle = 180
        break





