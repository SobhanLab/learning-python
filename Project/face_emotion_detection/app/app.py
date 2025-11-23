import streamlit as st
from PIL import Image
from utils import load_class_mapping, build_model, preprocess_image, predict_emotion

st.set_page_config(
    page_title="Face Emotion Detector",
    page_icon="😊",
    layout="centered",
)

EMOTION_FEEDBACK = {
    "Happy": "You look happy! Keep smiling, it suits you.",
    "Sad": "You seem a bit sad. It is okay to feel that way. Take care of yourself.",
    "Angry": "You look a bit angry. A short break and deep breathing can help.",
    "Fear": "There is some tension in your expression. Try to relax and ground yourself.",
    "Surprise": "You look surprised. Something unexpected must have happened.",
    "Disgust": "You look annoyed or uncomfortable. Stepping away can sometimes help.",
    "Neutral": "Your expression looks calm and neutral."
}

@st.cache_resource
def load_model_and_mapping():
    class_mapping = load_class_mapping("models/class_mapping.json")
    model = build_model(len(class_mapping), "models/emotion_model.pth")
    return model, class_mapping

def main():
    st.title("Face Emotion Detection")
    st.write(
        "Upload a face image and this app will predict an emotion using a pre-trained deep learning model."
    )

    try:
        model, class_mapping = load_model_and_mapping()
    except FileNotFoundError:
        st.error(
            "Pre-trained model file not found.\n\n"
            "Place your pre-trained weights at:\n"
            "`models/emotion_model.pth`"
        )
        st.stop()

    uploaded_file = st.file_uploader(
        "Upload a face photo (JPG/PNG)", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Detect Emotion"):
            with st.spinner("Analyzing emotion..."):
                input_tensor = preprocess_image(image)
                emotion, confidence = predict_emotion(input_tensor, model, class_mapping)

            st.subheader(f"Detected Emotion: {emotion}")
            st.write(f"Confidence: {confidence:.2f}")

            feedback = EMOTION_FEEDBACK.get(emotion)
            if feedback:
                st.info(feedback)

if __name__ == "__main__":
    main()
