import streamlit as st
import requests

st.title("Smart Text Analyzer")
text = st.text_area("Enter your text here...")

if st.button(label="Analyze"):
    if not text.strip():
        st.error("Please enter some text here")

    else:
        with st.spinner("Analyzing....."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"text": text}
            )
            if response.status_code == 200:
                data = response.json()

                st.write(f"Word Count: {data['word_count']}")
                st.write(f"Character Count: {data['character_count']}")
                st.write(f"Sentence Count: {data['sentence_count']}")
                st.write(f"Top Words: {data['top_words']}")
                st.write(f"Reading Time (min): {data['reading_time_minutes']}")
            
            else:
                
                st.error("Something went wrong")