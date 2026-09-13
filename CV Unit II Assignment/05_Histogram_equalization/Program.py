import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found!")
    exit()
equalized = cv2.equalizeHist(img)

cv2.imwrite("output.jpg", equalized)

hist_before = cv2.calcHist([img], [0], None, [256], [0, 256])

hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 6))

plt.plot(hist_before, label="Before Equalization")
plt.plot(hist_after, label="After Equalization")

plt.title("Histogram Before and After Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.legend()

plt.savefig("comparison.png")

plt.show()
