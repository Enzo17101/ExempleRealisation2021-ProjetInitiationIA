import cv2


img = cv2.imread('before.jpg',0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
after = cv2.Canny(blur,100,200)
cv2.imwrite('after.jpg',after)
cv2.waitKey(0)
cv2.destroyAllWindows()