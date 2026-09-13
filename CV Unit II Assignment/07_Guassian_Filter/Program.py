import cv2

img = cv2.imread("input.jpeg")

# 5x5 is chosen because it gives effective smoothing while preserving details reasonably well.
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite("Output.png", gaussian)
cv2.imshow("Original Noisy Image", img)
cv2.imshow("Gaussian Smoothed Image", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
