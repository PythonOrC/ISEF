# Blob Detection Example
#
# This example shows off how to use the find_blobs function to find color
# blobs in the image. This example in particular looks for dark green objects.

import sensor, image, time
from snake import Snake
from pid import PID
from pyb import UART

# You may need to tweak the above settings for tracking green things...
# Select an area in the Framebuffer to copy the color settings.

uart = UART(3, 9600)

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # turn this off.
clock = time.clock() # Tracks FPS.

# For color tracking to work really well you should ideally be in a very, very,
# very, controlled enviroment where the lighting is constant...
green_threshold   = (0, 100, -128, 95, 58, 127)
size_threshold = 2000
x_pid = PID(p=0.5, i=1, imax=100)
h_pid = PID(p=0.05, i=0, imax=50)
snake = Snake(0.1, 1)
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob

while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.

    blobs = img.find_blobs([green_threshold])
    if blobs:
        max_blob = find_max(blobs)
        x_error = max_blob[5]-img.width()/2
        h_error = max_blob[2]*max_blob[3]-size_threshold
        print("x error: ", x_error)
        '''
        for b in blobs:
            # Draw a rect around the blob.
            img.draw_rectangle(b[0:4]) # rect
            img.draw_cross(b[5], b[6]) # cx, cy
        '''
        img.draw_rectangle(max_blob[0:4]) # rect
        img.draw_cross(max_blob[5], max_blob[6]) # cx, cy
        x_output=x_pid.get_pid(x_error,1) + 20
        h_output=h_pid.get_pid(h_error,1)
        print("h_output",h_output)
        if x_output < -20:
            snake.forward()
        elif x_output > 20:
            snake.forward()


        '''
        if h_output > 0:
            car.run(0,h_output)
        if h_output < 0:
            car.run(h_output,0)
        '''


