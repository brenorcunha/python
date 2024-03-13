import numpy as np
from scipy.stats import mode
import cv2
import os
import csv
import time

cascade_trained = cv2.CascadeClassifier('/cascade.xml')
cascade_trained03 = cv2.CascadeClassifier('/cascade03.xml')

class Control:
    def main(self):
        # Load a classifier from a file
        aux = 0
        aux1 = 1
        largest = []
        # For each file in the list, do:

        # Load a video
        print("[INFO] Initializing webcam... ")
        cap = cv2.VideoCapture(0)
        cap.set(3, 800)  # Set width
        cap.set(4, 600)  # Set height

        while not cv2.waitKey(1) & 0xFF == ord('q'):
            aux = 0
            aux1 = 1
            # Load the video frame
            frameExists, frame = cap.read()

            #Reached the last frame or encountered an error? Then exit!
            if not frameExists:
                print("Something went wrong with the camera!!!")
                cap.release()
                return

            #Only works with grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Perform classifications
            cascade = cascade_trained.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
            cascade03 = cascade_trained03.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

            # Organize the classifications into a list for looping
            classifiers = [cascade, cascade03]

            for classifier in classifiers:
                test = format(len(classifier))
                aux1 = int(test)
                print("Data:", test)

                if aux1 > aux:
                    aux = aux1
                    print("Best Result:", aux)
                    largest = classifier

            # Draw rectangles around the objects
            for (x, y, w, h) in largest:
                # Draw a rectangle (image, initial position, final position, color, thickness)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                #roi_gray = gray[y:y+h, x:x+w]
                #roi_color = frame[y:y+h, x:x+w]
                #time.sleep(0.3)

            #Viewing detected frame: 
            cv2.imshow("detection", frame)            
        #Realease Webcam
        cap.release()
        #Close window
        cv2.destroyAllWindows()
        
control = Control()
control.main()
