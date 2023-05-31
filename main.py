import os
import glob
import sys
import cv2

SCALE_FACTOR = 1.01
MIN_NEIGHBORS = 5
MIN_SIZE = (15, 15)

FACIAL_DATABASE = [
    'haarcascade_frontalface_default.xml',
    'haarcascade_profileface.xml',
    'haarcascade_frontalface_alt2.xml',
]

def write_text(image, text):
    # Define the font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White color
    line_thickness = 2

    # Get the size of the text box
    text_size, _ = cv2.getTextSize(text, font, font_scale, line_thickness)

    # Calculate the coordinates to position the text at the bottom center
    text_x = int((image.shape[1] - text_size[0]) / 2)
    text_y = image.shape[0] - 20  # Adjust the value to change the vertical position

    # Add the text to the image
    cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, line_thickness)

def image_param():
    if len(sys.argv) > 1:
        # Access the arguments starting from index 1
        # sys.argv[0] is the script name itself
        arguments = sys.argv[1:]

        # Process the arguments
        return arguments
    else:
        return ['*.jpg', '*.jpeg', '*.png']

def load_images():
    # Create a list of image file extensions to filter
    image_extensions = image_param()

    # Use glob to get a list of image file paths in the folder
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join('input', extension)))

    return image_files

def save_image(image_file, image):
    # Save the processed image
    cv2.imwrite(os.path.join('output', os.path.basename(image_file)), image)

def detect_faces(image_file, face_cascade):
    # Load the image
    image = cv2.imread(image_file)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    write_text(image, f'Faces: {len(faces)}')

    save_image(image_file, image)

def run():
    # Load images
    image_files = load_images()

    # Load the pre-trained face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + FACIAL_DATABASE[2])

    # Iterate through the image files
    for image_file in image_files:
        detect_faces(image_file, face_cascade)

    # Close the OpenCV windows
    cv2.destroyAllWindows()

run()
