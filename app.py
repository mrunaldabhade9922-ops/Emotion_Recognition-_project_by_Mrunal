import streamlit as st

st.set_page_config(
    page_title="Emotion Recognition",
    layout="wide"
)

st.title("😊 Real-Time Emotion Recognition System")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("📷 Live Camera")
    st.info("Camera Feed will appear here.")

with col2:
    st.header("😀 Predicted Emotion")
    st.metric("Emotion", "Happy")

    st.subheader("Confidence")

    st.progress(92)

st.markdown("---")

st.subheader("Project Information")

st.write("""
- CNN Model
- TensorFlow
- OpenCV
- FER-2013 Dataset
- Real-Time Emotion Recognition
""")