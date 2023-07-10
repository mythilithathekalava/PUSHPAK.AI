
import cv2

import numpy as np

# Create a list to store the points
points = []

# Callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left button clicked
        points.append((x, y))
        
        if len(points) >= 2:
            # Draw a line between the last two points
            cv2.line(img, points[-2], points[-1], (0, 0, 255), 2)
            cv2.imshow("Image", img)

# Create a black image window
img = np.zeros((512,700,3), np.uint8)

# Create a window to display the image
cv2.namedWindow("Image")
cv2.imshow("Image", img)

# Set the mouse callback function
cv2.setMouseCallback("Image", mouse_callback)

# Wait for a key press and exit gracefully on 'q' key
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Close all windows
cv2.destroyAllWindows()
