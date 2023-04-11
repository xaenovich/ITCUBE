import cv2
import numpy as np

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cam = cv2.VideoCapture(0)

cv2.imshow("Image")

cv2.destroyAllWindows()
