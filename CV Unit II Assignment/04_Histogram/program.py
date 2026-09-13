import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Image not found!")
    exit()

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

highest_intensity = np.argmax(hist)

print("Intensity with highest frequency:", highest_intensity)

plt.figure(figsize=(10, 5))
plt.plot(hist)
plt.title("Grayscale Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])

plt.savefig("output.png")

plt.show()
