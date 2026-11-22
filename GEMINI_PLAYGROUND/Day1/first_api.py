
from google import genai
from dotenv import load_dotenv
import streamlit as st
import os
import base64

load_dotenv()

st.header("IaGemini")

input_text = st.text_input("Input:")

input_model = st.selectbox(
    "Select GEMINI Model:",
    [
        "gemini-4-hydrogen",
        "gemini-4-carbon",
        "gemini-3.8-flash",
        "gemini-nano-banana-2.1",
        "gemini-3.8-flash-tts"
    ]
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

if st.button("Submit"):

    if input_text.strip():

        try:
            with st.spinner("Gemini is generating response..."):

                interaction = client.interactions.create(
                    model=input_model,
                    input=input_text
                )
            st.subheader("Gemini Response")
            st.write(interaction.output_text)

        except Exception as e:
            st.error(f"Error: {type(e).__name__}: {e}")

    else:
        st.warning("Please enter some input.")
