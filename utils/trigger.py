def is_centered(box, frame_shape, threshold):
    h, w, _ = frame_shape

    x1, y1, x2, y2 = box
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    center_x = w // 2
    center_y = h // 2

    margin_x = int(w * threshold)
    margin_y = int(h * threshold)

    return (
        center_x - margin_x < cx < center_x + margin_x and
        center_y - margin_y < cy < center_y + margin_y
    )