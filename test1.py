import cv2
import numpy as np

if __name__ == '__main__':
   def callback(*arg):
       print (arg)

cv2.namedWindow( "result" )

img = cv2.imread("video.png")
hsv_min = np.array((24, 106, 220), np.uint8)
hsv_max = np.array((38, 219, 255), np.uint8)
hsv_min1 = np.array((0,0,213), np.uint8)
hsv_max1 = np.array((75,21,255), np.uint8)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    thresh1 = cv2.inRange(hsv, hsv_min1, hsv_max1)

    cv2.imshow('result', thresh)
    cv2.imshow('result', thresh1)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()