import cv2

def start_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise Exception("Camera not accessible")
    return cap