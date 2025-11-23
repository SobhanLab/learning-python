# Face Emotion Detection

This project is a simple face emotion detection web app built with a pre-trained deep learning model.

The app:

- Accepts an uploaded face image (JPG/PNG)
- Preprocesses the image to a fixed size
- Uses a pre-trained model to predict one of seven emotions:
  - Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral
- Displays a confidence score and a short feedback message

## Tech Stack

- Python
- PyTorch, Torchvision
- Streamlit
- Pillow

## Project Structure

```text
face_emotion_detection/
│
├─ app/
│   ├─ app.py
│   └─ utils.py
│
├─ models/
│   ├─ emotion_model.pth
│   └─ class_mapping.json
│
├─ requirements.txt
├─ README.md
└─ .gitignore
