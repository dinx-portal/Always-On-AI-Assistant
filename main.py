import streamlit as st
from tools import my_agent  # Ye line 'tools' folder se agent uthayegi

# App ki basic setting
st.set_page_config(page_title="My AI Factory", layout="wide")

# Sidebar Menu
st.sidebar.title("🚀 Navigation")
choice = st.sidebar.selectbox("Kahan jana hai?", ["Home", "My AI Agent"])

if choice == "Home":
    st.title("Welcome Boss! 🔥")
    st.write("Aapka personal AI system tayyar hai.")
    st.info("Sidebar se 'My AI Agent' select karein taake hum kaam shuru kar saken.")

elif choice == "My AI Agent":
    # Jab user ye select karega, toh my_agent.py wala code chalega
    my_agent.run()
