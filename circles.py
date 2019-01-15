import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], 0)
image = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 30, param1 = 50, param2 = 30, minRadius = 10, maxRadius = 80)

#altura da imagem
H = image.shape[0]
#largura da imagem
W = (image.shape[1]//2)

total = []

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
    #counting the circles
    total.append(i[0])

left = 0
right = 0
for n in total:
	if n < W: #largura
		left=left+1
	else:
		right=right+1

cv2.putText(gray,'Right:' + str(right), (15,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2, cv2.LINE_AA)
cv2.putText(gray,'Left:' + str(left), (15,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2, cv2.LINE_AA)

cv2.imshow('detected circles', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

