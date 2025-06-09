# app.py
import streamlit as st
from generator import generate_content

st.set_page_config(page_title="YouTube Content Generator", layout="wide")
st.title("🎬 YouTube Content Generator")
st.markdown("Generate video title, description, and script using AI")

topic = st.text_input("Enter video topic")
audience = st.text_input("Enter target audience")
tone = st.selectbox("Choose tone", ["Professional", "Casual", "Funny", "Motivational", "Friendly", "Informative"])
language = st.selectbox("Choose language", ["English", "Hindi", "Spanish", "French", "German", "Cantonese"])

if st.button("Generate"):
    if not topic or not audience:
        st.error("Please fill in both Topic and Audience.")
    else:
        with st.spinner("Generating..."):
            try:
                title, description, script = generate_content(topic, audience, tone, language)
                st.subheader("📌 Title")
                st.success(title)

                st.subheader("📝 Description")
                st.info(description)

                st.subheader("🎤 Script")
                st.code(script)

            except Exception as e:
                st.error(str(e))
