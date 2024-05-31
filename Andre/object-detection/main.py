

# pip install opencv-contrib-python # some people ask the difference between this and opencv-python
                                    # and opencv-python contains the main packages wheras the other
                                    # contains both main modules and contrib/extra modules
# pip install cvlib # for object detection

# # pip install gtts
# # pip install playsound
# use `pip3 install PyObjC` if you want playsound to run more efficiently.

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

from food_facts import food_facts
video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    # Bounding box.
    # the cvlib library has learned some basic objects using object learning
    # usually it takes around 800 images for it to learn what a phone is.
    bbox, label, conf = cv.detect_common_objects(frame)

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label}, and, ")
    else:
        new_sentence.append(f"a {label},")

    i += 1



for label in labels:
    try:
        print(f"\n\t{label.title()}")
        food_facts(label)

    except:
        print("No food facts for this item")