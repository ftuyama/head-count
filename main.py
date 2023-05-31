import os
import glob
import cv2

# Create a list of image file extensions to filter
image_extensions = ['*.jpg', '*.jpeg', '*.png']

# Use glob to get a list of image file paths in the folder
image_files = []
for extension in image_extensions:
    image_files.extend(glob.glob(os.path.join('images', extension)))

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iterate through the image files
for image_file in image_files:
    # Perform your desired operations on each image file
    print(image_file)

    # Load the image
    image = cv2.imread(image_file)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with detected faces
    cv2.imshow('Faces', image)
    cv2.waitKey(0)

    print(len(faces))


# Close the OpenCV windows
cv2.destroyAllWindows()
