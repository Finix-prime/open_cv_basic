import cv2
import numpy as np

while (True):
    img = cv2.imread("ball_mix.jpg")

    # kept color range /// np.array([B,G,R])
    lowwer = np.array([5, 111, 10])
    upper  = np.array([124, 255, 133])
    mask = cv2.inRange(img, lowwer, upper)
    result = cv2.bitwise_and(img, img, mask = mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("original", img)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", result)

cv2.destroyAllWindows()