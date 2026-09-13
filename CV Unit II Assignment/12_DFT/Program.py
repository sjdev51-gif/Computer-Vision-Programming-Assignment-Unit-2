import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

img_float = np.float32(img)

dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted_dft = np.fft.fftshift(dft)

print("Original Image Shape:", img.shape)
print("DFT Result Shape:", dft.shape)
print("Shifted DFT Shape:", shifted_dft.shape)
