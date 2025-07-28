import streamlit as st
import cv2
import numpy as np
import time
import os
import mediapipe as mp

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
### 🔓 Open Source | 🚀 Fast | 📸 Real-Time Camera

This open-source sign language detection system uses computer vision to detect hand gestures. 

### ✅ Features:
- Real-time hand detection with webcam
- Hand landmark tracking
- Dark, modern UI using Streamlit
- Live hand position display
""")

st.info("ℹ️ This is a hand detection demo. For full sign language recognition, you would need to train a custom model.")

# --- MediaPipe Setup ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# --- Webcam Setup ---
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
FRAME_WINDOW = st.image([])

# --- Hand Detection Loop ---
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    
    while True:
        success, frame = cap.read()
        if not success:
            st.error("⚠️ Failed to access camera.")
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the image and detect hands
        results = hands.process(frame_rgb)
        
        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                
                # Get hand position info
                h, w, _ = frame.shape
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)
                
                # Display hand position
                cv2.putText(frame, f"Hand detected at ({wrist_x}, {wrist_y})", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No hand detected", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the frame
        FRAME_WINDOW.image(frame, channels="BGR")

