import cv2
image =cv2.imread("C:\Users\Admin\Downloads\captain.jpg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert =cv2.bitwise_not(grey_img)
blur=cv2.GaussiamBlur(invert,(21,21),0)
invertedblur =cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur,scale=256.0)
cv2.imwrite("C:/Users/captain/Pictures/opencv/results.jpg",sketch) 