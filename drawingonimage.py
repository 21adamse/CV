import cv2

ghostimage = cv2.imread("images-opencv\ghost.png")

#drawing a line
linestart = (150,150)
lineend = (230,130)
linethickness = 6
linecolour = (0,0,0)
cv2.line(ghostimage,linestart,lineend,linecolour,linethickness)

linestart2 = (120,200)
lineend2 = (450,200)
glassescolour = (230,150,200)
cv2.line(ghostimage,linestart2,lineend2,glassescolour,linethickness)

linestart3 = (50,200)
lineend3 = (120,200)
cv2.line(ghostimage,linestart3,lineend3,glassescolour,linethickness)

#drawing a rectangle
topleftcorner1 = (330,120)
bottomrightcorner1 = (430,150)
recthickness = -2
reccolour = (0,0,0)
cv2.rectangle(ghostimage,topleftcorner1,bottomrightcorner1,reccolour,recthickness)

topleftcorner2 = (360,430)
bottomrightcorner2 = (410,520)
recthickness = -2
reccolour2 = (0,0,255)
cv2.rectangle(ghostimage,topleftcorner2,bottomrightcorner2,reccolour2,recthickness)

topleftcorner2 = (360,430)
bottomrightcorner2 = (410,520)
recthickness = -2
reccolour2 = (0,0,255)
cv2.rectangle(ghostimage,topleftcorner2,bottomrightcorner2,reccolour2,recthickness)


#drawing a circle
circlecentre = (250,350)
radius = 50
circlethickness = -5
circlecolour = (0,0,0)
cv2.circle(ghostimage,circlecentre,radius,circlecolour,circlethickness,lineType=cv2.LINE_4)

#drawing an arc
arcstart1 = (200,200)
arcend1 = (80,110)
angle = 0
startangle = 0
endangle = 180
arccolour = (0,0,0)
arcthickness = 8
arcstart2 = (380,200)
arcend2 = (70,110)
cv2.ellipse(ghostimage,arcstart1,arcend1,angle,startangle,endangle,glassescolour,arcthickness)
cv2.ellipse(ghostimage,arcstart2,arcend2,angle,startangle,endangle,glassescolour,arcthickness)

cv2.imshow("ghost image",ghostimage)

cv2.waitKey(0)
cv2.destroyAllWindows()