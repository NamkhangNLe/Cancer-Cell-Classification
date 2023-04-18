import cv2
import numpy as np
from matplotlib import pyplot as plt

# Take in image
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
  
# Image from RGB to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 30, minRadius = 40, maxRadius = 100)
  
# Draw circles that are detected.

lst = []
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)

        lst.append(r)

print(lst)

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(lst, bins = [0, 25, 50, 75, 100])
  
# Show plot
plt.show()
plt.ylabel('Probability')
plt.xlabel('Data')