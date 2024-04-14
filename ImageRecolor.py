import cv2
import numpy as np

# Load the image from "corshow.png": (0 loads in grayscale, 1 loads in color).
loaded_image = cv2.imread("corshow.png", 1)

# Display the loaded image in a window
cv2.imshow("Loaded Image:", loaded_image)

# Modify pixel values (in BGR order) at position (0, 0) for each color channel
loaded_image.itemset((0, 0, 2), 255)  # Set red channel to 255
loaded_image.itemset((0, 0, 1), 0)    # Set green channel to 0
loaded_image.itemset((0, 0, 0), 0)    # Set blue channel to 0

# Print image dimensions
print("Width in pixels:", loaded_image.shape[1])
print("Height in pixels:", loaded_image.shape[0])
print("Number of channels:", loaded_image.shape[2])

# Get color values of the pixel at (0, 0)
print("Red channel value:", loaded_image.item(0, 0, 2))
print("Green channel value:", loaded_image.item(0, 0, 1))
print("Blue channel value:", loaded_image.item(0, 0, 0))

# Save the modified image
cv2.imwrite("output_image.jpg", loaded_image)

# Crop a region of interest (ROI) from the loaded image
cropped_region = loaded_image[180:250, 250:315]  # (yi:yf, xi:xf)
cv2.imwrite("cropped_image.jpg", cropped_region)

# Resize the image (600x600 pixels and double the original size)
resized_image = cv2.resize(loaded_image, (600, 600))
resized_image = cv2.resize(loaded_image, (int(loaded_image.shape[1] * 2), int(loaded_image.shape[0] * 2)))

# Draw a green rectangle on detected elements
for (x, y, w, h) in green_elements:
    cv2.rectangle(loaded_image, (x, y), (x + w, y + h), (0, 255, 0), 4)

# Display the modified image
cv2.imshow("Modified Image:", loaded_image)

# Wait for user input (0 waits indefinitely)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
