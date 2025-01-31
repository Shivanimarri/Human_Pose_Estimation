import cv2
import mediapipe as mp

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load an image
image_path = "pose-best-case-image-png-format.png"  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load image.")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform pose estimation
    results = pose.process(image_rgb)

    # Draw landmarks only (no lines)
    if results.pose_landmarks:
        print("Pose landmarks detected!")

        # Extract landmark data
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            print(f"Landmark {idx}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")

        # Get image dimensions
        h, w, c = image.shape
        
        for landmark in results.pose_landmarks.landmark:
            # Convert normalized coordinates to pixel coordinates
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            
            # Draw the keypoints
            cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)  # Green color, filled circle

    # Display the output image
    cv2.imshow("Pose Landmarks", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Release resources
pose.close()