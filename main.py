import cv2
import time

from models.yolo_model import load_model
from detection.dog_detector import detect_dog
from tracking.stability_tracker import StabilityTracker
from utils.camera import start_camera
from utils.image_utils import save_image
from utils.trigger import is_centered

import config


def main():
    print("🚀 Starting Auto Dog Photographer...")

    # Load model
    model = load_model()

    # Start camera
    cap = start_camera(config.CAMERA_INDEX)

    if not cap.isOpened():
        print("❌ Camera not opening")
        return

    tracker = StabilityTracker(
        config.STABILITY_FRAMES,
        config.MOVEMENT_THRESHOLD
    )

    captured = False

    while True:
        ret, frame = cap.read()

        if not ret:
            print("❌ Failed to grab frame")
            break

        # Detect dogs
        dogs = detect_dog(model, frame, config.CONFIDENCE_THRESHOLD)

        for box in dogs:
            x1, y1, x2, y2 = box

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Update tracker
            tracker.update(box)

            # Check conditions
            centered = is_centered(box, frame.shape, config.CENTER_THRESHOLD)
            stable = tracker.is_stable()

            # Display status
            status = f"Centered: {centered}, Stable: {stable}"
            cv2.putText(frame, status, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            # 🔥 CAPTURE CONDITION
            if centered and stable and not captured:
                print("📸 CAPTURE TRIGGERED!")

                captured_frame = frame.copy()

                # Save image
                save_image(captured_frame, config.SAVE_PATH)

                captured = True

                # 🔥 SHOW IMAGE AND WAIT FOR USER
                while True:
                    display_frame = captured_frame.copy()

                    cv2.putText(display_frame, "📸 Press SPACE to continue", (30, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    cv2.imshow("Auto Dog Photographer 🐶📸", display_frame)

                    key = cv2.waitKey(1)

                    # SPACE → resume camera
                    if key == 32:
                        break

                    # ESC → exit program
                    if key == 27:
                        cap.release()
                        cv2.destroyAllWindows()
                        return

                # reset after viewing
                captured = False
                tracker.positions.clear()

        # Show live feed
        cv2.imshow("Auto Dog Photographer 🐶📸", frame)

        # Exit on ESC
        if cv2.waitKey(1) == 27:
            print("👋 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()