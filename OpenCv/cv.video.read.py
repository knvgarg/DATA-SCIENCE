# Read a video stream from camera(frame by frame)

import cv2

cap = cv2.VideoCapture(0) # to select a webcam, 0 is default webcam(you can give id if there are multiple webcams)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret, frame = cap.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	# returns 2 values (1. boolean -> if frame was properly captured or there was an error )
	#					2. frame itself

	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5) # (frame, scalefactor, minNieghbours)
	# returns list of tuples containing (x_coord, y_coord, width, height)

	
	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("video Frame", frame)


	# Wait for user input - q, then you wil stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF		# wait for 1 milisec

	# here cv2.waitKey(1) returns 32 bit value while ord gives 8 bit retun value
	# hence we AND the result of waitkey with 0xFF(which is 8 '1s') to get an 8 bit number saved in our variable

	if key_pressed == ord('q'):		# ord is a method that converts to ASCII value
		break

cap.release() # Release the device
cv2.destroyAllWindows()

""" 
scaleFactor - parameter specifying how much the image size is reduced at each image scale.

Basically scale factor is used to create your scale pyramid.

in 1.05 is a good scale factor, which means you use a small step for resizing i.e reduce size

minNieghbours - parameter specifying how many Nieghbours each candidate rectangle should retain it.,
this parameter will affect the quality of the detected faces higher value results in less detection but will higher quality.
3~6  is agood value for it

"""