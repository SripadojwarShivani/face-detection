# import libraries
import cv2
import face_recognition

# capturing video from webcam
video_capture = cv2.VideoCapture(0)

# Initializing list for face locations
face_locations = []

while True:
    # Taking a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR to RGB 
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Drawing BBoxes around the faces
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()