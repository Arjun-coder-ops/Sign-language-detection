import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import pyttsx3
import time
import os

# Paths
model_path = "model/keras_model.h5"
labels_path = "model/labels.txt"

# Initialize
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier(model_path, labels_path)

# Voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index if no sound
engine.setProperty('rate', 150)

# Read labels
with open(labels_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]

last_label = ""
last_time = time.time()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        crop = img[y:y+h, x:x+w]

        try:
            crop = cv2.resize(crop, (224, 224))
            prediction, index = classifier.getPrediction(crop)
            label = labels[index]

            if label != last_label and time.time() - last_time > 1:
                print("Detected:", label)
                engine.say(label)
                engine.runAndWait()
                last_label = label
                last_time = time.time()

            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        except Exception as e:
            print("Resize error:", e)

    # Full screen window
    cv2.namedWindow("Sign Detection", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Sign Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Sign Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
