import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# Aapki API Key
genai.configure(api_key="AIzaSyAdII8duUsYhJjxb6v7hum_CC7hh1owzJk")

def run():
    st.subheader("🤖 Aapka Personal AI Agent")
    
    if 'active' not in st.session_state:
        st.session_state.active = False

    if st.button("Activate Agent" if not st.session_state.active else "Deactivate Agent"):
        st.session_state.active = not st.session_state.active

    if st.session_state.active:
        st.success("Agent Online Hai! 🟢")
        prompt = st.chat_input("Hukum karein Boss...")
        
        if prompt:
            # Is format se 404 error khatam ho jayega
            try:
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                response = model.generate_content(prompt)
                
                st.chat_message("user").write(prompt)
                st.chat_message("assistant").write(response.text)
                
                # Voice output
                tts = gTTS(text=response.text, lang='hi')
                tts.save("reply.mp3")
                st.audio("reply.mp3", format="audio/mp3", autoplay=True)
            except Exception as e:
                st.error(f"Ek aur koshish: {e}")
                # Agar phir bhi masla ho toh ye backup model try karega
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt)
                st.chat_message("assistant").write(response.text)
    else:
        st.info("Agent is Offline. Button dabayein.")
