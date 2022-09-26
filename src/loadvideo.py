#!/usr/bin/env python

from imutils import video
VideoStream = video.VideoStream
import numpy as np
import argparse
import imutils

import time
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.python.keras.preprocessing import image


imgSize = 32

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame1 = vs.read()
    frame = cv2.resize(frame1, (imgSize, imgSize))

    test_image = image.img_to_array(frame)
    test_image = np.expand_dims(test_image, axis = 0)     
      

    # show the output frame
    cv2.imshow("Frame", frame1)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # update the FPS counter


# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

