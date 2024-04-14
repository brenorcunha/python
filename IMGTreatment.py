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
