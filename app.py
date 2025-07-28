import streamlit as st
import cv2
import numpy as np
import pyttsx3
import time
import os
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

# --- Streamlit Config ---
st.set_page_config(page_title="Sign Language Detection", layout="wide")

# --- Custom CSS for Modern Dark UI ---
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .main {
        background-color: #1e1e1e;
        color: white;
    }
    header, footer, .css-18e3th9 {
        background-color: #1e1e1e;
        color: white;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.title("🤟 Real-Time Sign Language Detection")
st.markdown("""
### 🔓 Open Source | 🚀 Fast | 🎤 Voice Enabled | 📸 Real-Time Camera

This open-source sign language detection system uses machine learning and computer vision to recognize hand gestures from American Sign Language (ASL). It supports the following signs:

- 👋 **Hello**
- ❤️ **I Love You**

### ✅ Features:
- Real-time gesture detection with webcam
- Converts gesture to text and speech
- Minimal lag using OpenCV and cvzone
- Voice output with pyttsx3
- Dark, modern UI using Streamlit
- Black screen showing detected gesture
""")

st.warning("⚠️ Currently trained for only 2 signs: 'Hello' and 'I Love You'. More coming soon!")

# --- Voice Engine Setup ---
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# --- Load Model ---
model_path = os.path.join("model", "keras_model.h5")
labels_path = os.path.join("model", "labels.txt")

if not os.path.exists(model_path) or not os.path.exists(labels_path):
    st.error("❌ Model files not found. Make sure keras_model.h5 and labels.txt exist in 'model/' folder.")
    st.stop()

classifier = Classifier(model_path, labels_path)
detector = HandDetector(maxHands=1)

# --- Webcam Setup ---
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
FRAME_WINDOW = st.image([])

# --- State Variables ---
last_prediction = ""
last_spoken_time = 0

# --- App Loop ---
while True:
    success, frame = cap.read()
    if not success:
        st.error("⚠️ Failed to access camera.")
        break

    hands, frame = detector.findHands(frame)
    prediction = ""
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        cropped = frame[y-20:y+h+20, x-20:x+w+20]
        cropped = cv2.resize(cropped, (224, 224))
        cropped = np.expand_dims(cropped, axis=0)
        cropped = np.array(cropped, dtype=np.float32)
        cropped = cropped / 255.0
        
        prediction, index = classifier.getPrediction(cropped, draw=False)
        
        if prediction[index] > 0.9:
            label = classifier.labels[index]
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            current_time = time.time()
            if label != last_prediction or current_time - last_spoken_time > 3:
                engine.say(label)
                engine.runAndWait()
                last_prediction = label
                last_spoken_time = current_time
    
    # Display black screen with text
    black_img = np.zeros((200, 640, 3), dtype=np.uint8)
    if last_prediction:
        cv2.putText(black_img, f"Detected: {last_prediction}", (50, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

    combined_img = np.vstack((frame, black_img))
    FRAME_WINDOW.image(combined_img, channels="BGR")

