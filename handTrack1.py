import cv2 as cv
import numpy as np
import autodistill

class HandDetector:
    def __init__(self, model):
        self.model = model

    def detect_hands(self, img):
        results = self.model(img)
        return results

    def findHands(self, img, draw=True):
        detections = self.detect_hands(img)
        if draw:
            for box in detections:
                x, y, w, h = box['box']
                cv.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        detections = self.detect_hands(img)
        if len(detections) != 0:
            box = detections[handNo]
            x, y, w, h = box['box']
            lmList.append([0, int(x + w / 2), int(y + h / 2)])
        return lmList

    def fingersUp(self):
        # Dummy logic to simulate fingers up detection
        return [1, 1, 0, 0, 0]
