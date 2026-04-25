import numpy as np

DOG_CLASS_ID = 16  # COCO class for dog

def detect_dog(model, frame, conf_threshold):
    results = model(frame)[0]

    dogs = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])

        if cls_id == DOG_CLASS_ID and conf > conf_threshold:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            dogs.append((x1, y1, x2, y2))

    return dogs