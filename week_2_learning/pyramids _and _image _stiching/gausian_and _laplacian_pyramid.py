import cv2
img=cv2.imread("week_2_learning\pyramids _and _image _stiching\img2.jpg")

if img is None:
    print("image is empty , provide image or correct path")

g1=cv2.pyrDown(img)
g2=cv2.pyrDown(g1)
g3=cv2.pyrDown(g2)
g4=cv2.pyrDown(g3)

expanded=cv2.pyrUp(g2)
expanded_resized=cv2.resize(expanded,(g1.shape[1],g1.shape[0]))#changes the shape of expanded accordinh to the g1

loss=cv2.subtract(g1, expanded_resized)

cv2.imshow("original image",img)
cv2.imshow("level 1",g1)
cv2.imshow("level 2",g2)
cv2.imshow("level 3",g3)
cv2.imshow("level 4",g4)
cv2.imshow("laplacian pyramid showing loss in image deta",loss)
cv2.waitKey(0)
cv2.destroyAllWindows()