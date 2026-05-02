import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# Tumhari API Key yahan set kar di hai
genai.configure(api_key="AIzaSyAdII8duUsYhJjxb6v7hum_CC7hh1owzJk")

def run():
    st.subheader("🤖 Aapka Personal AI Agent")
    
    # Agent ki state check karna
    if 'active' not in st.session_state:
        st.session_state.active = False

    # Start aur Stop button
    if st.button("Activate Agent" if not st.session_state.active else "Deactivate Agent"):
        st.session_state.active = not st.session_state.active

    if st.session_state.active:
        st.success("Agent Online Hai! 🟢 (Ab aap mujhse baat kar sakte hain)")
        
        # User input box
        prompt = st.chat_input("Hukum karein Boss...")
        
        if prompt:
            # Gemini Model call karna
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('Agent soch raha hai...'):
                response = model.generate_content(prompt)
            
            # Chat interface mein dikhana
            st.chat_message("user").write(prompt)
            st.chat_message("assistant").write(response.text)
            
            # Voice Generation (Awaaz mein jawab)
            try:
                tts = gTTS(text=response.text, lang='hi')
                tts.save("reply.mp3")
                st.audio("reply.mp3", format="audio/mp3", autoplay=True)
                # Purani audio file delete karna taake memory full na ho
                os.remove("reply.mp3")
            except Exception as e:
                st.info("Audio mein thodi der lag rahi hai, lekin text upar maujood hai.")
    else:
        st.info("Agent is Offline. Upar wala button daba kar ise On karein.")
