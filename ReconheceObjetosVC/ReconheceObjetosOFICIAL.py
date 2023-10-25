import numpy as np
from scipy.stats import mode
import cv2
import os
import csv
import time
import pathlib

class Control:
    #Takes the paths automatically:
    path = os.path.dirname(os.path.abspath(__file__)) +'\\In'
    path1 = os.path.dirname(os.path.abspath(__file__)) +'\\positive'
    path2 = os.path.dirname(os.path.abspath(__file__)) +'\\negative'
    path3 = os.path.dirname(os.path.abspath(__file__)) +'\\Out'
    maior = [] #Declaring variable to keep the best detection data.
    os.chdir(path)
    def menu(self):
        txt = """
        Opções:
            1-Webcam Face Recognition;
            2-Photo Face Recognition;
            3-Train your own cascade (for recognition of a specific object); 
            4-Recognition with the trained cascade;
            5-Exit;
        Type your option:
        """
        option = int(input(txt))
        return option
    #Function iterating over the options:
    def main(self):
        options = {1:self.option1, 2:self.option2, 3:self.option3, 4:self.option4}
        while True:
            option = self.menu()
            if option in options:
                options[option]()
            else:
                if option == 5:
                  break
                else:
                  print("Invalid option!")
                  
    def option1(self):
        maior = []
        #loads a classifier from a file
        aux = 0
        aux1= 1

        #For each file in list, do:
        #Loads a video:
        print("[INFO] Initializing webcam... ")
        cap = cv2.VideoCapture(0)
        cap.set(3, 800) # Set width
        cap.set(4, 600) # Set height

        while(not cv2.waitKey(1) & 0xFF == ord('q')):
            aux = 0
            aux1= 1
            #Loads the video frame
            frameExists, frame = cap.read()
            
            #Did you reach the last frame or was there an error? So get out!
            if(frameExists == False):
                print("Something is wrong with the webcam!!!")
                cap.release()
                return
            
            #Only works with grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #Classifying and setting classifiers: 
            faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50,50))
            faces2 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50,50))
            faces3 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50,50))
            faces4 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50,50))

            classifiers = [faces, faces2, faces3, faces4]

            for (classifier) in classifiers:
                test = format(len(classifier))
                aux1 = int(test)
                print("Faces:",test)
                if aux1 > aux:
                   aux = aux1
                   print ("Best result:",aux)
                   maior = (classifier)
				     
            #For each detected face: 
            for (x, y, w, h) in maior:
                #Draw a rectangle (image, start position, end position, color, thickness)
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 2)
                #time.sleep(0.3)
            
            cv2.imshow("Detected", frame)
            
        #Turn webcam off and close window
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()

    def option2(self):
        #=== Paths ===
        #path ../In
        #path1 ../training/positive
        #path2 ../training/negative
        #path3 ../Out
        
        maior = []
        file_list = []
        file_list = search_folder(control.path,".jpg")

        if  len(file_list) != 0:
            for file in file_list:
                print("[INFO] Fetching the images in the default folder... ")
                aux = 0
                aux1= 1
                #For each file in folder, do:
                #Reads the image and converts to grayscale: 
                img = cv2.imread(file)
                half = cv2.resize(img, (500, 500))
                gray = cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
                            
                #classifiying:
                faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
                faces2 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
                faces3 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
                faces4 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))

                faces5 = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
                faces6 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
                faces7 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))
                faces8 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(20,20))

                classifiers = [faces, faces2, faces3, faces4,faces5, faces6, faces7, faces8]

                for (classifier) in classifiers:
                    test = format(len(classifier))
                    aux1 = int(test)
                    print("Faces:",test)
                    if aux1 > aux:
                       aux = aux1
                       print ("Best result:",aux)
                       maior = (classifier)
                       
                #Put the squares in faces
                for (x,y,w,h) in maior:
                    cv2.rectangle(half,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = half[y:y+h, x:x+w]
                              
                #Displays images with rectangles, saves image with rectangles
                #if it doesn't exist, only shows if it exists

                os.chdir(control.path3) #Current path
                existe = pathlib.Path(file)
                                      
                if existe.exists() is True:
                    cv2.imshow('half',half)
                    print("For the file "+file+", {0} faces were found!".format(len(maior)))
                else:
                    cv2.imshow('half',half)
                    print("For the file "+file+", {0} faces were found!".format(len(maior)))
                    cv2.imwrite(file,half)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                os.chdir(control.path)
               
            cv2.destroyAllWindows()
            #control.Out.close()
        else:
            print("[INFO] Empty folder ")

    def option3(self):
        #=== Paths ===
        #path ../In
        #path1 ../positive
        #path2 ../negative
        #path3 ../Out

        file_list = []
        file_list_positive = []
        file_list_negative = []
        
        file_list = search_folder(control.path,".jpg")
        file_list_positive = search_folder(control.path1,".jpg")
        file_list_negative = search_folder(control.path2,".jpg")

        tratamentoIMG(control.path1,file_list_positive,"positive",50)
        tratamentoIMG(control.path2,file_list_negative,"negative",100)
        
        positiveDescriptors()
        negativeDescriptors()

        #Create sample:
        mycmd="opencv_createsamples -img dado5050.jpg -bg bg.txt -info Out/info.lst -pngoutput Out -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1950" 
        
        #Create Vector File of Positive Detections: 
        mycmd1 = "opencv_createsamples -info Out/info.lst -num 1950 -w 20 -h 20 -vec positives.vec"

        #Real training:
        mycmd2 = "opencv_traincascade -data Out -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20"

        os.system(mycmd)
        os.system(mycmd1)
        os.system(mycmd2)
                
    def option4(self):
        file_list = []
        file_list = search_folder(control.path,".jpg")
        
        if  len(file_list) != 0:
            for file in file_list:
                print("[INFO] Fetching the images in the default folder... ")
                aux = 0
                aux1= 1
                #For every file in folder, do:
                #reads the image and converts to grayscale:
                img = cv2.imread(file)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            
                #Classifying and setting classifiers: 
                cascade = cascade_treinado.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
                
                classifiers = [cascade]

                for (classifier) in classifiers:
                    test = format(len(classifier))
                    aux1 = int(test)
                    print("Objetos:",test)
                    
                #Put the squares in images: 
                for (x,y,w,h) in classifier:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]
                              
                #Displays images with rectangles, saves image with rectangles
                #if it doesn't exist, only shows if it exists
                os.chdir(control.path3) #Current folder.
                existe = pathlib.Path(file)
                                      
                if existe.exists():
                    cv2.imshow('img',img)
                    print("For the file "+file+", {0} objects were found!".format(len(classifier)))
                else:
                    cv2.imshow('img',img)
                    print("For the file "+file+", {0} objects were found!".format(len(classifier)))
                    cv2.imwrite(file,img)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                os.chdir(control.path)
               
            cv2.destroyAllWindows()
        else:
            print("[INFO] Empty folder ")

#=================================================
#======== GLOBAL VARIABLES AND METHODS ============
#=================================================
            
#Establishes the face classifiers: 

#Turn to the trained cascade: 
cascade_treinado = cv2.CascadeClassifier('../haarcascades/cascade.xml')

face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
face_alt_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt.xml')
face_alt2_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
face_alt_tree_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt_tree.xml')


def tratamentoIMG(path,file_list,tipo,tamanho):
    pic_num=0
    os.chdir(path)
    #negative image processing:
    if  len(file_list) != 0:
        print("[INFO] Searching in folder",tipo)
        for file in file_list:
            img = cv2.imread(file)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized_img = cv2.resize(gray, (tamanho, tamanho))
            cv2.imwrite(tipo+str(pic_num)+ ".jpg", resized_img)
            #print("Echo!")
            pic_num+=1
    else:
        print("[INFO] Pasta",tipo,"Vazia ")

#Searching for files in folder: 
def search_folder(diretorio,extensao):
    file_list = []
    for file in os.listdir(diretorio):
        if file.endswith(extensao):
            file_list.append(file)
            #print(file)
    return file_list

def negativeDescriptors():
    print("[INFO] Creating Negative Descriptors (They don't have the target object)")
    for file_type in [control.path2]:
        for img in os.listdir(file_type):
            if file_type == control.path2:
                line = file_type+'/'+img+'\n'
                os.chdir(control.path)
                with open('bg.txt','a') as f:
                    f.write(line)
                
def positiveDescriptors():
    print("[INFO] Creating Positive Descriptors (They have the target object)")
    for file_type in [control.path1]:
        for img in os.listdir(file_type):
            if file_type == control.path1:
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                os.chdir(control.path)
                with open('info.dat','a') as f:
                    f.write(line)

        
control = Control()
control.main()
