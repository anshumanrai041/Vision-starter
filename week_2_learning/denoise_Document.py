import cv2
import numpy as np
kernel=np.ones((3,3),np.uint8)
img = cv2.imread("week_2_learning/images_used/document7.webp")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

denoised = cv2.medianBlur(gray, 3)


_, thresh = cv2.threshold(
    denoised,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

erosion=cv2.dilate(thresh,kernel,iterations=1)
cv2.imshow("original image",img)
cv2.imshow("Result", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()