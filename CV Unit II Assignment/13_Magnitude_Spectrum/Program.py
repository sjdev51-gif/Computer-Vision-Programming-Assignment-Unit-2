import cv2
import numpy as np


img = cv2.imread("input.jpeg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

magnitude = 20 * np.log(magnitude + 1)
spectrum = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow("Original Image", img)
cv2.imwrite("Output.png", spectrum.astype(np.uint8))
