import streamlit as st
import cv2
import numpy as np
import time

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
st.title("🤟 Real-Time Webcam Feed")
st.markdown("""
### 🔓 Open Source | 🚀 Fast | 📸 Real-Time Camera

This is a basic webcam feed application that demonstrates real-time video processing.

### ✅ Features:
- Real-time webcam feed
- Basic motion detection
- Dark, modern UI using Streamlit
- Live video display
""")

# --- Camera Access Check ---
@st.cache_resource
def check_camera():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        cap.release()
        return ret
    return False

camera_available = check_camera()

if not camera_available:
    st.warning("⚠️ Camera not available. This might be because:")
    st.markdown("""
    - You're running this on Streamlit Cloud (remote server)
    - Camera permissions are not granted
    - No camera is connected
    
    **Demo Mode**: Showing a sample image instead.
    """)
    
    # Create a demo image
    demo_img = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.putText(demo_img, "Camera Demo", (200, 240), 
               cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    cv2.putText(demo_img, "Camera not available", (150, 280), 
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(demo_img, "This is a demo image", (180, 320), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    
    st.image(demo_img, channels="BGR", caption="Demo Image - Camera Not Available")
    
    st.info("💡 To test with real camera, run this locally with: `streamlit run app.py`")
    
else:
    st.success("✅ Camera detected! Starting live feed...")
    
    # --- Webcam Setup ---
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    FRAME_WINDOW = st.image([])

    # --- Motion Detection Variables ---
    prev_frame = None
    motion_threshold = 25

    # --- Video Processing Loop ---
    while True:
        success, frame = cap.read()
        if not success:
            st.error("⚠️ Failed to access camera.")
            break

        # Flip the frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert to grayscale for motion detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        # Initialize prev_frame if it's None
        if prev_frame is None:
            prev_frame = gray
            continue
        
        # Calculate frame difference
        frame_delta = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(frame_delta, motion_threshold, 255, cv2.THRESH_BINARY)[1]
        
        # Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # Find contours on thresholded image
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw motion detection info
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter small contours
                motion_detected = True
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display status
        if motion_detected:
            cv2.putText(frame, "Motion Detected!", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No Motion", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Update prev_frame
        prev_frame = gray
        
        # Display the frame
        FRAME_WINDOW.image(frame, channels="BGR")

