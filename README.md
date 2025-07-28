# 🤟 Sign Language Detection

A real-time sign language detection system that uses machine learning and computer vision to recognize American Sign Language (ASL) gestures from webcam input.

## ⚠️ Important: Camera Access

**Streamlit Cloud Limitation**: This app cannot access your webcam when deployed on Streamlit Cloud due to remote server limitations.

**For Real Camera Testing**: Run the app locally on your computer.

## ✨ Features

- **Real-time Detection**: Live webcam feed with instant gesture recognition
- **Voice Output**: Converts detected signs to speech using text-to-speech
- **Modern UI**: Clean, dark-themed interface built with Streamlit
- **Multiple Signs**: Currently supports 4 ASL signs:
  - 👋 **Hello**
  - ❤️ **I Love You** 
  - 🙏 **Thank You**
  - ❌ **No**
- **Open Source**: Fully open-source and customizable

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam (for local testing)
- Windows 10/11 (tested on Windows)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arjun-coder-ops/Sign-language-detection.git
   cd SignLanguage-Detection
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv sign_venv
   # On Windows:
   sign_venv\Scripts\activate
   # On macOS/Linux:
   source sign_venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application LOCALLY**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`
   - **Allow camera access** when prompted
   - Your webcam will work for real sign detection!

## 🌐 Streamlit Cloud Deployment

The app is also deployed on Streamlit Cloud for demonstration purposes:

- **URL**: [Your Streamlit Cloud URL]
- **Note**: Camera access is limited on cloud deployment
- **Demo Mode**: Shows sample images and instructions

## 📁 Project Structure

```
SignLanguage-Detection/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── model/
│   ├── keras_model.h5    # Trained ML model
│   └── labels.txt        # Sign labels
└── sign_images/
    ├── Hello.jpg         # Example images
    └── I_Love_You.jpg
```

## 🛠️ Dependencies

- **Streamlit**: Web application framework
- **OpenCV**: Computer vision and image processing
- **cvzone**: Hand tracking and classification
- **pyttsx3**: Text-to-speech conversion
- **TensorFlow**: Machine learning framework
- **NumPy**: Numerical computing
- **Pillow**: Image processing

## 🎯 How It Works

1. **Hand Detection**: Uses MediaPipe through cvzone to detect hand landmarks
2. **Image Processing**: Crops and preprocesses the hand region
3. **Classification**: Feeds processed image to trained Keras model
4. **Output**: Displays detected sign and converts to speech

## 📊 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 224x224 pixels
- **Training Data**: Custom dataset of ASL signs
- **Accuracy**: Optimized for real-time performance

## 🎮 Usage

### Local Testing (Recommended)
1. **Start the app**: Run `streamlit run app.py`
2. **Position your hand**: Hold your hand in front of the camera
3. **Make signs**: Perform any of the supported ASL signs
4. **Listen**: The app will speak the detected sign
5. **Watch**: See the detection results on screen

### Cloud Deployment
1. **Visit the Streamlit Cloud URL**
2. **View demo mode**: See sample images and instructions
3. **Follow local setup**: Use the instructions to run locally

## 🔧 Customization

### Adding New Signs

1. Collect training images for new signs
2. Retrain the model with new data
3. Update `model/labels.txt` with new labels
4. Replace `model/keras_model.h5` with new model

### Modifying UI

- Edit the CSS in `app.py` for different styling
- Modify the Streamlit components for layout changes

## 🐛 Troubleshooting

### Common Issues

**Camera not working locally:**
- Ensure camera permissions are granted
- Check if another application is using the camera
- Try restarting the application

**Camera not working on Streamlit Cloud:**
- This is expected - cloud servers cannot access local webcams
- Use local testing for real camera functionality

**Model not loading:**
- Verify `model/keras_model.h5` and `model/labels.txt` exist
- Check file permissions

**Dependencies issues:**
- Recreate virtual environment
- Update pip: `pip install --upgrade pip`
- Install dependencies individually if needed

### Performance Tips

- Close other applications using the camera
- Ensure good lighting for better hand detection
- Keep hand clearly visible in camera frame

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs**: Open an issue with detailed description
2. **Suggest features**: Propose new signs or improvements
3. **Submit code**: Fork the repo and create a pull request
4. **Improve documentation**: Help make this README better

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Hand tracking powered by [MediaPipe](https://mediapipe.dev/)
- Machine learning with [TensorFlow](https://tensorflow.org/)
- Computer vision with [OpenCV](https://opencv.org/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues
3. Create a new issue with detailed information

---

**Made with ❤️ for the deaf and hard-of-hearing community** 