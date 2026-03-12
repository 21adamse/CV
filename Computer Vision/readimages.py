import cv2

#loading the image
pika = cv2.imread("opencv-assets-main\pika.png")

#dispaying the image
cv2.imshow("Image",pika)

#holding the window
cv2.waitKey(0)

#deleting from RAM
cv2.destroyAllWindows()