import numpy as np

class StabilityTracker:
    def __init__(self, max_frames, movement_threshold):
        self.positions = []
        self.max_frames = max_frames
        self.threshold = movement_threshold

    def update(self, box):
        x1, y1, x2, y2 = box
        center = ((x1 + x2)//2, (y1 + y2)//2)

        self.positions.append(center)

        if len(self.positions) > self.max_frames:
            self.positions.pop(0)

    def is_stable(self):
        if len(self.positions) < self.max_frames:
            return False

        movements = []

        for i in range(1, len(self.positions)):
            dx = abs(self.positions[i][0] - self.positions[i-1][0])
            dy = abs(self.positions[i][1] - self.positions[i-1][1])
            movements.append(dx + dy)

        avg_movement = np.mean(movements)

        return avg_movement < self.threshold