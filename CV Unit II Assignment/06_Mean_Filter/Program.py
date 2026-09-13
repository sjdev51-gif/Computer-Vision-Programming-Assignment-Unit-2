import cv2

img = cv2.imread("input.jpeg")
if img is None:
    print("Image not found!")
    exit()
kernel1 = (3, 3)
filtered_3x3 = cv2.blur(img, kernel1)

kernel2 = (7, 7)
filtered_7x7 = cv2.blur(img, kernel2)

cv2.imwrite("Output.png", filtered_7x7)

cv2.imshow("Original Image", img)
cv2.imshow("Mean Filter 3x3", filtered_3x3)
cv2.imshow("Mean Filter 7x7", filtered_7x7)

cv2.waitKey(0)
cv2.destroyAllWindows()
