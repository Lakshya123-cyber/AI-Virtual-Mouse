



import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
import requests
cap = cv2.VideoCapture(0)
ret, imgOriginalScene = cap.read()

# wCam, hCam = 640, 480


url = "http://192.168.1.73:8888/shot.jpg"

img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
imgOriginalScene = cv2.imdecode(img_arr, -1)



cv2.imshow("IPcamera", imgOriginalScene)
cv2.namedWindow("IPcamera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("IPcamera", 300, 300)

# cap = cv2.VideoCapture(url)
# cap.set(3, wCam)
# cap.set(4, hCam)
# pTime = 0
# detector = htm.handDetector(maxHands=1)
# wScr, hScr = pyautogui.size()
# print(wScr, hScr)

# while True:
    # success, img = cap.read()
    # img = detector.findHands(img)
    # lmList, bbox = detector.findPosition(img)

    # if len(lmList) != 0:
    #     x1, y1 = lmList[8][1:]
    #     x2, y2 = lmList[12][1:]
    #     # print(x1, y1, x2, y2)

    #     fingers = detector.fingersUp()
    #     # print(fingers)

    #     if fingers[1] == 1 and fingers[2] == 0:
    #         x3 = np.interp(x1, (0, wCam), (0, wScr))
    #         y3 = np.interp(y1, (0, hCam), (0, hScr))

    #         pyautogui.move(x3, y3)

    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    # cv2.imshow("Image", img)
    # cv2.waitKey(1)