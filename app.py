import streamlit as st
import cv2
import numpy as np
import time
import os

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
st.title("🤟 Sign Language Detection")
st.markdown("""
### 🔓 Open Source | 🚀 Fast | 📸 Real-Time Camera

This is a sign language detection system that recognizes ASL gestures from webcam input.

### ✅ Features:
- Real-time sign detection with webcam
- Supports 4 ASL signs: Hello, I Love You, Thank You, No
- Dark, modern UI using Streamlit
- Voice output for detected signs
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
    st.warning("⚠️ **Camera Not Available**")
    st.markdown("""
    ### Why can't I access my camera?
    
    This app is running on **Streamlit Cloud** (a remote server), which cannot access your local webcam for security reasons.
    
    ### How to test with real camera:
    
    1. **Clone the repository**:
       ```bash
       git clone https://github.com/Arjun-coder-ops/Sign-language-detection.git
       cd SignLanguage-Detection
       ```
    
    2. **Install dependencies**:
       ```bash
       pip install -r requirements.txt
       ```
    
    3. **Run locally**:
       ```bash
       streamlit run app.py
       ```
    
    4. **Allow camera access** when prompted in your browser
    
    ### What you'll see here:
    - Real sign language images showing how to make each sign
    - Instructions for local setup
    - Sample sign language images
    """)
    
    # Create demo content with actual sign images
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Supported ASL Signs")
        
        # Load and display actual sign images
        sign_images = {
            "Hello": "sign_images/Hello.jpg",
            "I Love You": "sign_images/I_Love_You.jpg", 
            "Thank You": "sign_images/Thank_You.jpg",
            "No": "sign_images/No.jpg"
        }
        
        for sign_name, image_path in sign_images.items():
            if os.path.exists(image_path):
                st.image(image_path, caption=f"ASL Sign: {sign_name}", use_column_width=True)
            else:
                # Fallback if image doesn't exist
                demo_img = np.zeros((200, 300, 3), dtype=np.uint8)
                cv2.putText(demo_img, f"Sign: {sign_name}", (50, 100), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                st.image(demo_img, caption=f"Demo: {sign_name}", use_column_width=True)
    
    with col2:
        st.subheader("🎯 How It Works")
        st.markdown("""
        ### Detection Process:
        1. **Hand Detection**: Uses MediaPipe to detect hand landmarks
        2. **Image Processing**: Crops and preprocesses hand region
        3. **Classification**: Feeds image to trained CNN model
        4. **Output**: Displays detected sign and speaks it
        
        ### Supported Signs:
        - 👋 **Hello** - Wave your hand
        - ❤️ **I Love You** - Thumb, index, and pinky extended
        - 🙏 **Thank You** - Fingers touching chin, then moving forward
        - ❌ **No** - Index finger pointing up, moving side to side
        
        ### Tips for Best Detection:
        - Ensure good lighting
        - Keep your hand clearly visible
        - Make signs slowly and clearly
        - Position hand in center of camera view
        """)
    
    st.info("💡 **Pro Tip**: Run this locally to test with your real webcam and see actual sign detection in action!")
    
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

