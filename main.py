import numpy as np
from PIL import ImageGrab
import cv2
def process_img(image):
    original_image = image
    hsv_min = np.array((21, 13, 217), np.uint8)
    hsv_max = np.array((179, 255, 255), np.uint8)
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    processed_img = cv2.inRange(processed_img, hsv_min, hsv_max)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    return processed_img
def main():
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()