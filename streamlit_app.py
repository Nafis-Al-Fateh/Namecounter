import streamlit as st

st.title("Name Character Counter")

# Input box
student = st.text_input("Please Input Your Name:")

if student:
    dictionary = {student: len(student)}

    st.write("### Your Name:")
    st.write(student)

    st.write("### Dictionary:")
    st.json(dictionary)
