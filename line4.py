import numpy as np
import cv2
import time
import pyautogui
from directkeys import PressKey, ReleaseKey, W, A, S, D
from drow_lanes import draw_lanes
from grabscreen import grab_screen


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(image):
    original_image = image
    hsv_min = np.array((21, 13, 217), np.uint8)
    hsv_max = np.array((179, 255, 255), np.uint8)
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    processed_img = cv2.inRange(processed_img, hsv_min, hsv_max)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)
    processed_img = roi(processed_img, [vertices])
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 180, 20, 15)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1, m2 = draw_lanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)


            except Exception as e:
                print(str(e))
    except Exception as e:
        pass
    return processed_img, original_image, m1, m2

t_time = 0.07

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)
def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)
def slow_ya_roll():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
    last_time = time.time()
    while True:
        screen = grab_screen(region=(0, 40, 800, 640))
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        new_screen, original_image, m1, m2 = process_img(screen)
        cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()