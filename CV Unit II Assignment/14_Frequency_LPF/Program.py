import cv2
import numpy as np

img = cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE)

img_float = np.float32(img)
dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.float32)

radius = 50
cv2.circle(mask, (ccol, crow), radius, (1, 1), -1)

filtered_dft = dft_shift * mask
dft_inverse_shift = np.fft.ifftshift(filtered_dft)

reconstructed = cv2.idft(dft_inverse_shift)

reconstructed = cv2.magnitude(reconstructed[:, :, 0], reconstructed[:, :, 1])
reconstructed = np.uint8(reconstructed)

cv2.imwrite("output.png", reconstructed)

cv2.imshow("Original Image", img)
cv2.imshow("Low-Pass Filtered Image", reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
