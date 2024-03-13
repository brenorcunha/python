import numpy as np
from scipy.stats import mode
import cv2
import os
import csv
import time
path="C:/Users/breno/python"
os.chdir(path)

#Save the file with the title updated by date and hour.
title = time.strftime("%Y-%m-%d") + '_' + time.strftime("%H-%M-%S")
output = open('face_recon_'+title+'.csv', 'w')
export = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)

biggest=0
file_list = []

for file in os.listdir(path):
    if file.endswith(".jpg"):
        file_list.append(file)
        #print(file_list)
for file in file_list:
    aux =0
    aux1 =1
    #Stablish face classifiers
    face_cascade = cv2.CascadeClassifier('./FaceAndObjectsRecognition/haarcascades/haarcascade_frontalface_default.xml')
    face_alt_cascade = cv2.CascadeClassifier('./FaceAndObjectsRecognition/haarcascades/haarcascade_frontalface_alt.xml')
    face_alt2_cascade = cv2.CascadeClassifier('./FaceAndObjectsRecognition/haarcascades/haarcascade_frontalface_alt2.xml')
    face_alt_tree_cascade = cv2.CascadeClassifier('./FaceAndObjectsRecognition/haarcascades/haarcascade_frontalface_alt_tree.xml')

    #Reads the image and converts to grayscale
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Perform the classifications
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces2 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces3 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    faces4 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))

    faces5 = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
    faces6 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
    faces7 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
    faces8 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))

    #Store classifications in a loop
    classifiers = [faces, faces2, faces3, faces4, faces5, faces6, faces7, faces8]

    #Tests which classifier is the best
    for classifier in classifiers:
        test = format(len(classifier))
        aux1 = int(test)
        print("Faces:",test)
        if aux1 > aux:
            aux = aux1
            print ("Best result:", aux)
            biggest = (classifier)
            
    #for (classifier) in classifiers:
        #Put the squares in the faces
        for (x,y,w,h) in biggest:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

    print("Para a image "+ file +", foram encontradas {0} faces!".format(len(biggest)))
    #Displays the squared images
    cv2.imshow('img',img)
    cv2.waitKey(0)

    #Displays the mean, variance and mode of each classifier
    found = []

    for (classifier) in classifiers:
        x = format(len(classifier))
        found.append(x)

    found = np.asarray(found, dtype = np.float16)
    mean = np.mean(found)
    variance = np.var(found)
    mode = float(mode(found)[0])

    if file == file_list[0]:
        export.writerow(["image","mean","variance","mode"])
        export.writerow([file, mean, variance, mode])
    else:
        export.writerow([file, mean, variance, mode])

cv2.destroyAllWindows()
output.close()
