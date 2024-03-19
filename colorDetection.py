class ulColor(object):
    import os
    import numpy as np
    import cv2

class Control:
    def menu(self):
        txt = """
        CHOOSE THE COLOR TO BE DETECTED: 
            1-Red
            2-Green
            3-Blue
            4-Exit
        Enter your choice: 
        """
        option = int(input(txt))
        return option

    # MAIN FUNCTION: PROMPTS FOR IMAGE NAME AND CONVERTS IT TO HSV
    def main(self):
        while True:
            # Input and search for the image name (it needs to be in the same folder as the .py file)
            # img = input("Enter the image name with extension, e.g., img.ext: ")
            # file = os.path.realpath(img)

            global image, image1
            image = cv2.imread('corshow.png')
            image1 = cv2.imread('corshow.png')

            # Convert from BGR to HSV
            try:
                global hsv
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV
                break
            except:
                print("Image not found")

    # MENU FOR COLOR DETECTION AND RESULT GENERATION
    def option1(self):
        # Detect RED
        ulColor.maskRes(ulColor.rColor(0, 10, 10), ulColor1.rColor(200, 255, 255))

    def option2(self):
        # Detect GREEN
        ulColor.maskRes(ulColor.rColor(20, 20, 20), ulColor1.rColor(80, 255, 255))

    def option3(self):
        # Detect BLUE
        ulColor.maskRes(ulColor.rColor(75, 100, 100), ulColor1.rColor(150, 255, 255))

# Class that handles mask processing: 
    #Setting up color detection range.
    def rColor(self, h, s, v):
        self.rangeUL = np.array([h,s,v],np.uint8)
        return self.rangeUL

    # Generates the mask, asks for two instances of the class to use the above method: 
    def maskRes(self, ulColor, ulColor1):    
        #GENERATE MASK
        mask = cv2.inRange(hsv, ulColor, ulColor1)
        mask = cv2.GaussianBlur(mask, (1, 1), 0)
        res = cv2.bitwise_and(image,image, mask=mask)
        res0 = cv2.bitwise_and(image,image, mask=mask)
        
        #GENERATE REVERSE MASK
        reverse_mask = cv2.bitwise_not(mask)
        res1 = cv2.bitwise_and(image,image, mask=reverse_mask)
        
        zeros = np.zeros(res.shape[:2], dtype = "uint8")
        test = cv2.bitwise_not(mask)
        
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        antiAliasing = cv2.GaussianBlur(gray, (7, 7), 0)
        
        borders = cv2.Canny(reverse_mask, 5, 150)
        (objects, lx) = cv2.findContours(borders.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw Yellow Outline on Inverted Mask (20,202,255)
        t2 = cv2.drawContours(image1, objects, -1, (20,202, 255), 2)
        #cv2.imshow("Number of objects: "+str(len(objects)), image)
        
        # Splitting the selected area into RGB channels
        (blueChannel, greenChannel, redChannel) = cv2.split(res)
        
        res1 = cv2.bitwise_and(image,image, mask=reverse_mask)
        test = cv2.bitwise_not(mask)
        
        v1 = -1
        v2 = -1
        v3 = -1
        
        while (v1 <0 or v1 >255): 
            v1 = int(input("Enter Multiplier for Channel [RED] Between 0 and 255: "))
        while (v2 <0 or v2 >255): 
            v2 = int(input("Enter Multiplier for Channel [GREEN] Between 0 and 255: "))
        while (v3 <0 or v3 >255): 
            v3 = int(input("Enter Multiplier for Channel [BLUE] Between 0 and 255: "))
        
        #JOIN THE BGR AND APPLIES MULTIPLICATION
        res = cv2.merge([blueChannel*v3, greenChannel*v2, redChannel*v1])
        
        #Join: The Inverted mask and the REcolored area.
        final = cv2.add(res,res1)
        #final = cv2.add(res,image)
        
        temp = np.vstack([
            np.hstack([t2, res0]),
            np.hstack([res, final]),
            ])

        #temp1 = np.vstack([np.hstack([mask, reverse_mask]),])
        cv2.imshow("Original image: ", image)
        cv2.imshow("Quantity of objects: "+str(len(objects)), temp)
        #cv2.imshow("MN", temp1)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows

#Instances: 
ulColor = ulColor()
ulColor1 = ulColor()
control = Control()
control.main()
