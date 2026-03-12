import cv2

image = cv2.imread("images-opencv/videocollage1.jpg")

#converting to greyscale
greyimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("BG",image)
cv2.waitKey(0)
cv2.imshow("GreyBG",greyimage)
cv2.waitKey(0)

#loading coloured image as greyscale
greyimage2 = cv2.imread("images-opencv/videocollage3.jpg",0)
cv2.imshow("GreyBG2",greyimage2)

cv2.waitKey(0)
cv2.destroyAllWindows()
