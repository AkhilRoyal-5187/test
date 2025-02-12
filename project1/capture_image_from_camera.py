import cv2
import os

# Set camera port (0 is default for most webcams)
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# Get the name input from the user
inp = input("Enter person name: ").strip()

# Ensure the input name is valid
if not inp:
    print("Error: Name cannot be empty.")
    cam.release()
    cv2.destroyAllWindows()
    exit()

# Check if the camera is working
if not cam.isOpened():
    print("Error: Unable to access the camera. Please check the connection.")
    cam.release()
    cv2.destroyAllWindows()
    exit()

# Directory to save the images
known_faces_dir = 'known_faces'

# Ensure the 'known_faces' directory exists
if not os.path.exists(known_faces_dir):
    os.makedirs(known_faces_dir)

print("Press 's' to save an image or 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    if not ret:
        print("Error: Failed to capture image. Exiting.")
        break

    # Display the frame in a window
    cv2.imshow(f"Capturing - {inp}", frame)

    # Use waitKey with a 10ms delay to ensure key press detection
    key = cv2.waitKey(10)

    if key == ord('s'):  # Save the image
        filename = f"{inp}.png"
        filepath = os.path.join(known_faces_dir, filename)
        success = cv2.imwrite(filepath, frame)
        if success:
            print(f"Image saved as {filepath}")
        else:
            print("Error: Failed to save the image.")
        break  # Exit loop after saving
    elif key == ord('q'):  # Exit without saving
        print("Exiting without saving.")
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
