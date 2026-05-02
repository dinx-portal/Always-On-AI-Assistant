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
            # Model ka naam update kar diya hai taake error khatam ho jaye
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            try:
                response = model.generate_content(prompt)
                st.chat_message("user").write(prompt)
                st.chat_message("assistant").write(response.text)
                
                # Voice output (Audio generate karna)
                tts = gTTS(text=response.text, lang='hi')
                tts.save("reply.mp3")
                st.audio("reply.mp3", format="audio/mp3", autoplay=True)
            except Exception as e:
                # Agar koi aur masla ho toh yahan dikhayega
                st.error(f"Ek choti si mushkil hui hai: {e}")
    else:
        st.info("Agent is Offline. Upar wala button dabayein.")
