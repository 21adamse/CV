import cv2

image1 = cv2.imread("images-opencv/videocollage1.jpg")
image2 = cv2.imread("images-opencv/videocollage2.jpg")
imagecombined = cv2.addWeighted(image1,0.5,image2,0.5,1)

cv2.imshow("Image1",image1)
cv2.waitKey(0)
cv2.imshow("Image2",image2)
cv2.waitKey(0)
cv2.imshow("Image3",imagecombined)
cv2.waitKey(0)
cv2.destroyAllWindows()