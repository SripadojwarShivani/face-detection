# import libraries
import cv2
import face_recognition

#reading an image
img = cv2.imread('/home/shivanisri/Desktop/Shivani/AI/face detection/test2.jpg')

# Initializing list as face locations
face_locations = []

# Convert the image from BGR to RGB .
rgb_img = img[:, :, ::-1]

# Find all the faces in the image
face_locations = face_recognition.face_locations(rgb_img)

# Drawing bounding boxes around faces
for top, right, bottom, left in face_locations:
    # Draw a box around the face
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the results
cv2.imshow('image', img)
cv2.waitKey(0)