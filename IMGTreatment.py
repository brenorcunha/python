import numpy as np
import cv2

image = cv2.imread('A.jpg')
image1 = cv2.imread('A.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([20, 20, 20], np.uint8)
upper_green = np.array([80, 255, 255], np.uint8)

mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)

mask_inv = cv2.bitwise_not(mask)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
smoothed = cv2.GaussianBlur(gray, (7, 7), 0)

edges = cv2.Canny(mask_inv, 5, 150)
(objects, _) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
t2 = cv2.drawContours(image1, objects, -1, (255, 0, 0), 1)

res1 = cv2.bitwise_and(image, image, mask=mask_inv)

(blue_channel, green_channel, red_channel) = cv2.split(res)

zeros = np.zeros(res.shape[:2], dtype="uint8")
test = cv2.bitwise_not(mask)

res = cv2.merge([zeros, green_channel, zeros])

test = cv2.add(res, res1)

cv2.imshow("RES", test)
cv2.imshow("MN", mask)
cv2.imshow("MI", mask_inv)

cv2.imshow("Number of objects: ", t2)

# cv2.imshow("Red", cv2.merge([zeros, zeros, red_channel]))
# cv2.imshow("Green", cv2.merge([zeros, green_channel, zeros]))
# cv2.imshow("Blue", cv2.merge([blue_channel, zeros, zeros]))

# Extracting colors from channels based on specified percentages. 1% B, 0% G, 90% RED (In this case, only the green channel was used, divided into 3).
# cv2.imshow("Green Channel", cv2.merge([r * 0, g * 0, b * 0]))
# Now we should use the other colors through an inverted mask, i.e., it will capture everything that is non-green and complement it in the image.
cv2.waitKey(0)
cv2.destroyAllWindows()

###=============IMAGE TREATMENT (Another code):==================================
##import cv2
##import numpy as np
##
### Load the image from "corshow.png": (0 loads in grayscale, 1 loads in color).
##loaded_image = cv2.imread("corshow.png", 1)
##
### Display the loaded image in a window
##cv2.imshow("Loaded Image:", loaded_image)
##
### Modify pixel values (in BGR order) at position (0, 0) for each color channel
##loaded_image.itemset((0, 0, 2), 255)  # Set red channel to 255
##loaded_image.itemset((0, 0, 1), 0)    # Set green channel to 0
##loaded_image.itemset((0, 0, 0), 0)    # Set blue channel to 0
##
### Display the modified image
##cv2.imshow("Modified Image:", loaded_image)
##
### Wait for user input (0 waits indefinitely)
##cv2.waitKey(0)
##
### Close all windows
##cv2.destroyAllWindows()
##
### Print image dimensions
##print("Width in pixels:", loaded_image.shape[1])
##print("Height in pixels:", loaded_image.shape[0])
##print("Number of channels:", loaded_image.shape[2])
##
### Get color values of the pixel at (0, 0)
##print("Red channel value:", loaded_image.item(0, 0, 2))
##print("Green channel value:", loaded_image.item(0, 0, 1))
##print("Blue channel value:", loaded_image.item(0, 0, 0))
##
### Save the modified image
##cv2.imwrite("output_image.jpg", loaded_image)
##
### Crop a region of interest (ROI) from the loaded image
##cropped_region = loaded_image[180:250, 250:315]  # (yi:yf, xi:xf)
##cv2.imwrite("cropped_image.jpg", cropped_region)
##
### Resize the image (600x600 pixels and double the original size)
##resized_image = cv2.resize(loaded_image, (600, 600))
##resized_image = cv2.resize(loaded_image, (int(loaded_image.shape[1] * 2), int(loaded_image.shape[0] * 2)))
##
### Draw a green rectangle on detected elements
##for (x, y, w, h) in green_elements:
##    cv2.rectangle(loaded_image, (x, y), (x + w, y + h), (0, 255, 0), 4)
