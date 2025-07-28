# 🚀 Deploy to Replit with Camera Access

This guide will help you deploy your Sign Language Detection app to Replit, where users can access their webcam.

## 📋 Prerequisites

1. **Replit Account**: Sign up at [replit.com](https://replit.com)
2. **GitHub Repository**: Your code is already on GitHub

## 🎯 Step-by-Step Deployment

### Step 1: Create New Repl
1. Go to [replit.com](https://replit.com)
2. Click **"Create Repl"**
3. Choose **"Python"** as the language
4. Name it: `sign-language-detection`

### Step 2: Import Your Code
1. In your new Repl, click **"Version Control"** in the left sidebar
2. Click **"Import from GitHub"**
3. Enter your repository URL: `https://github.com/Arjun-coder-ops/Sign-language-detection`
4. Click **"Import from GitHub"**

### Step 3: Configure Dependencies
1. Replace the contents of `requirements.txt` with:
   ```
   streamlit>=1.28.0
   opencv-python-headless>=4.8.0
   numpy>=1.24.0
   Pillow>=10.0.0
   replit>=3.3.0
   ```

2. Or use the `requirements_replit.txt` file

### Step 4: Set Main File
1. Rename `replit_app.py` to `main.py` (or keep as is)
2. Make sure it's set as the main file

### Step 5: Configure Replit
1. Create a `.replit` file with:
   ```toml
   language = "python3"
   run = "streamlit run replit_app.py --server.port 8501 --server.address 0.0.0.0"
   ```

2. Create a `pyproject.toml` file with:
   ```toml
   [tool.poetry]
   name = "sign-language-detection"
   version = "0.1.0"
   description = "Sign Language Detection with Camera Access"
   authors = ["Your Name"]

   [tool.poetry.dependencies]
   python = "^3.8"
   streamlit = "^1.28.0"
   opencv-python-headless = "^4.8.0"
   numpy = "^1.24.0"
   Pillow = "^10.0.0"
   replit = "^3.3.0"
   ```

### Step 6: Deploy
1. Click **"Run"** in Replit
2. Wait for dependencies to install
3. Your app will be available at the provided URL

## ✅ Features on Replit

- ✅ **Camera Access**: Users can access their webcam
- ✅ **Real-time Detection**: Live sign language detection
- ✅ **Python Support**: Full Python environment
- ✅ **Free Hosting**: No cost for basic usage
- ✅ **Easy Sharing**: Share URL with others

## 🔧 Troubleshooting

### Camera Not Working
1. **Allow Permissions**: Click "Allow" when prompted for camera access
2. **Refresh Page**: Sometimes needed for camera to initialize
3. **Check Browser**: Make sure you're using a modern browser

### Dependencies Issues
1. **Restart Repl**: Sometimes fixes dependency issues
2. **Check Requirements**: Make sure all packages are listed
3. **Update Python**: Replit supports Python 3.8+

### Performance Issues
1. **Close Other Tabs**: Free up resources
2. **Restart Repl**: Clears memory
3. **Check Internet**: Stable connection needed

## 🌐 Sharing Your App

Once deployed, you can:
1. **Share the URL** with others
2. **Embed in websites** using iframe
3. **Use for demos** and presentations

## 📱 Mobile Access

Replit apps work on mobile browsers, but camera access may be limited on some devices.

## 🎯 Advantages of Replit

- ✅ **Camera Access**: Unlike Streamlit Cloud
- ✅ **Python Support**: Full Python environment
- ✅ **Free Tier**: No cost for basic usage
- ✅ **Easy Deployment**: One-click deployment
- ✅ **Real-time Updates**: Changes deploy instantly

## 🔗 Your App URL

Once deployed, your app will be available at:
`https://your-repl-name.your-username.repl.co`

Users can access their camera and test sign language detection in real-time! 