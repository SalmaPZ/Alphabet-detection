#Importing all the important models and install them if not installed on your device
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os, ssl, time



#Fetching the data
//add code(rfer step 1)


#Splitting the data and scaling it
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, train_size=3500, test_size=500)
#scaling the features
X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0

#Fitting the training data into the model
clf = LogisticRegression(solver='saga', multi_class='multinomial').fit(X_train_scaled, y_train)

#Calculating the accuracy of the model
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("The accuracy is :- ",accuracy)

# #Starting the camera
 cap = cv2.VideoCapture(0)
 print("camera started")
 while(True):
#   # Capture frame-by-frame
  try:
     ret, frame = cap.read()
     print("Inside the loop")
    # # Our operations on the frame come here
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # #Drawing a box in the center of the video
     height, width = gray.shape
     upper_left = (int(width / 2 - 56), int(height / 2 - 56))
     bottom_right = (int(width / 2 + 56), int(height / 2 + 56))
     cv2.rectangle(gray, upper_left, bottom_right, (0, 255, 0), 2)

    # #To only consider the area inside the box for detecting the digit
   # #roi = Region Of Interest
     //add code(step 2)

     #Converting cv2 image to pil format
     im_pil = Image.fromarray(roi)

    # # convert to grayscale image - 'L' format means each pixel is 
    # # represented by a single value from 0 to 255
    //add code(step 3)

#     # Display the resulting frame
     cv2.imshow('frame',gray)
     if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   except Exception as e:
     pass

# # When everything done, release the capture
 cap.release()
 cv2.destroyAllWindows()


