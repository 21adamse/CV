import cv2

image = cv2.imread("images-opencv\opencv.png")
blues  ,greens  ,reds = cv2.split(image)

image2 = cv2.imread("images-opencv/bilateral.jpg")
blues2  ,greens2  ,reds2 = cv2.split(image2)

cv2.imshow("Original",image)
cv2.waitKey(0)

cv2.imshow("Blue",blues)
cv2.waitKey(0)

cv2.imshow("Green",greens)
cv2.waitKey(0)

cv2.imshow("Red",reds)
cv2.waitKey(0)

cv2.imshow("Original2",image2)
cv2.waitKey(0)

cv2.imshow("Blue2",blues2)
cv2.waitKey(0)

cv2.imshow("Green2",greens2)
cv2.waitKey(0)

cv2.imshow("Red2",reds2)
cv2.waitKey(0)

cv2.destroyAllWindows()