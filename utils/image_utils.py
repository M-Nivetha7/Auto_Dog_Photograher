import cv2
import os
import time

def save_image(frame, path):
    if not os.path.exists(path):
        os.makedirs(path)

    filename = f"{path}/dog_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved: {filename}")

    show_captured_image(frame)

    return filename


def show_captured_image(image):
    # Create a dedicated window
    cv2.namedWindow("Captured Photo 📸", cv2.WINDOW_NORMAL)

    start_time = time.time()

    while True:
        cv2.imshow("Captured Photo 📸", image)

        # wait 1 ms and check key
        key = cv2.waitKey(1)

        # close on ESC or after 3 seconds
        if key == 27 or (time.time() - start_time) > 3:
            break

    cv2.destroyWindow("Captured Photo 📸")