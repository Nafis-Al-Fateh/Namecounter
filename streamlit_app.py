import streamlit as st

# Page Config
st.set_page_config(page_title="Name Character Counter", page_icon="✨", layout="centered")

# Custom CSS for background and styling
page_bg = """
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

/* Title styling */
h1 {
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
    color: #ffdd57;
    font-size: 48px;
    text-shadow: 2px 2px 5px black;
}

/* Input box styling */
.stTextInput > div > div > input {
    background-color: #f0f8ff;
    color: black;
    border-radius: 10px;
    padding: 10px;
    font-size: 18px;
}

/* Info cards */
.result-box {
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1>✨ Name Character Counter ✨</h1>", unsafe_allow_html=True)

# Input
student = st.text_input("✍️ Please Input Your Name:")

# Results
if student:
    length = len(student)

    st.markdown(f"<div class='result-box'>✅ Your Name: {student}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'>📏 Character Count: {length}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'>📝 Dictionary: { {student: length} }</div>", unsafe_allow_html=True)

    st.progress(min(length, 20) / 20)
else:
    st.markdown("<div class='result-box'>👆 Please enter a name above to see results</div>", unsafe_allow_html=True)
